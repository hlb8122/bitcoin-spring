# Bitcoin Spring (WIP)

Bitcoin Spring is a small scalable service which allows client to subscribe to filtered streams of transactions or blocks.

# Example

```python
from spring_pb2_grpc import SubscriberStub, grpc
from spring_pb2 import Regex

# Initialize client
channel = grpc.insecure_channel('127.0.0.1:50051')
stub = SubscriberStub(channel)

# Create regex to query stream from
regex = Regex(regex=".*")

# Iterate over stream
for matches in stub.Subscribe(regex):
    print(matches.matches)
```
