fn main() {
    tower_grpc_build::Config::new()
        .enable_server(true)
        // .enable_client(true)
        .build(&["proto/spring.proto"], &["proto"])
        .unwrap_or_else(|e| panic!("protobuf compilation failed: {}", e));
    println!("cargo:rerun-if-changed=proto/spring.proto");
}
