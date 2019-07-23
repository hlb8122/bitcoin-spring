use std::{
    collections::HashMap,
    sync::{Arc, Mutex},
};

use bitcoin_zmq::{SubFactory, Topic};
use bus_queue::async_::{channel, Subscriber};
use regex::bytes::Regex as Re;
use tokio::{net::TcpListener, prelude::*};
use tower_grpc::{Request, Response};
use tower_hyper::server::{Http, Server};

use crate::spring::{server, Matches, Regex};

pub mod spring {
    include!(concat!(env!("OUT_DIR"), "/spring.rs"));
}

#[derive(Clone)]
struct Spring {
    pub factory: Arc<SubFactory>,
    pub publishers: Arc<Mutex<HashMap<String, Subscriber<Matches>>>>,
}

impl server::Subscriber for Spring {
    type SubscribeFuture =
        future::FutureResult<Response<Self::SubscribeStream>, tower_grpc::Status>;
    type SubscribeStream = Box<dyn Stream<Item = Matches, Error = tower_grpc::Status> + Send>;

    fn subscribe(&mut self, request: Request<Regex>) -> Self::SubscribeFuture {
        // Create Regex
        let reg_str = &request.get_ref().regex;
        let regex: Re = match Re::new(reg_str) {
            Ok(ok) => ok,
            Err(_) => {
                return future::err(tower_grpc::Status::new(
                    tower_grpc::Code::InvalidArgument,
                    "regex malformed",
                ))
            }
        };

        // Subscribe if publisher exists, else create new publisher first
        let mut publishers_guard = self.publishers.lock().unwrap();
        let new_stream = match publishers_guard.get(reg_str) {
            Some(some) => some.clone(),
            None => {
                let new_stream = self
                    .factory
                    .subscribe(Topic::RawTx)
                    .filter_map(move |arc_vec| {
                        let matches: Vec<Vec<u8>> = regex
                            .captures_iter(&arc_vec[..])
                            .map(|c| c.get(0).unwrap().as_bytes().to_vec())
                            .collect();
                        if !matches.is_empty() {
                            Some(Matches { matches })
                        } else {
                            None
                        }
                    });
                let (new_publisher, broker) = broadcast(new_stream, 1024);
                tokio::spawn(broker);
                let new_stream = new_publisher.clone();
                publishers_guard.insert(reg_str.clone(), new_publisher);
                new_stream
            }
        };

        let new_stream = new_stream
            .map(|x| (*x).clone())
            .map_err(|_| tower_grpc::Status::new(tower_grpc::Code::Internal, "internal error"));
        future::ok(Response::new(Box::new(new_stream)))
    }
}

fn main() {
    // Declare subscriber
    let (factory, broker) = SubFactory::new("tcp://127.0.0.1:28332", 1024);
    let broker = broker.map_err(|_| ());

    // Declare Spring service
    let factory = Arc::new(factory);
    let spring = Spring {
        factory,
        publishers: Arc::new(Mutex::new(HashMap::new())),
    };
    let new_service = server::SubscriberServer::new(spring);
    let mut server = Server::new(new_service);
    let http = Http::new().http2_only(true).clone();

    // Bind
    let addr = "127.0.0.1:50051".parse().unwrap();
    let bind = TcpListener::bind(&addr).expect("bind");

    println!("spring at {:?}", addr);

    // Connection future
    let serve = bind
        .incoming()
        .for_each(move |sock| {
            if let Err(e) = sock.set_nodelay(true) {
                return Err(e);
            }

            let serve = server.serve_with(sock, http.clone());
            tokio::spawn(serve.map_err(|e| println!("h2 error: {:?}", e)));

            Ok(())
        })
        .map_err(|e| eprintln!("accept error: {}", e));

    tokio::run(serve.join(broker).map(|_| ()));
}

#[inline]
pub fn broadcast<B>(
    stream: impl Stream<Item = B, Error = ()>,
    buffer: usize,
) -> (Subscriber<B>, impl Future<Item = (), Error = ()>)
where
    B: Send,
{
    let (incoming, broadcast) = channel(buffer);
    let broker = incoming
        .sink_map_err(|_| ())
        .send_all(stream)
        .and_then(|_| Ok(()));
    (broadcast, broker)
}
