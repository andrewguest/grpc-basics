import grpc
from greeting_pb2 import GreetingRequest
from greeting_pb2_grpc import GreeterStub

channel = grpc.insecure_channel("localhost:50051")
client = GreeterStub(channel)

request = GreetingRequest(
    name="Andrew"
)

greeting_message = client.sayHello(request)

print(greeting_message)
