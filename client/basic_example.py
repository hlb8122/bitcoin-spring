from spring_pb2_grpc import SubscriberStub, grpc
from spring_pb2 import Regex

# Initialize client
channel = grpc.insecure_channel('127.0.0.1:50051')
stub = SubscriberStub(channel)

# Create regex to filter stream
regex = Regex(regex=".*")

# Iterate over stream
for matches in stub.Subscribe(regex):
    print(matches.matches)
