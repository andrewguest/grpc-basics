from concurrent.futures import ThreadPoolExecutor

import grpc
from greeting_pb2 import GreetingRequest
from greeting_pb2_grpc import GreeterStub

channel = grpc.insecure_channel("localhost:50051")
client = GreeterStub(channel)
request = GreetingRequest(
    name="Andrew"
)

executor = ThreadPoolExecutor(max_workers=5)
a = executor.submit(client.sayHello, request)
b = executor.submit(client.sayHello, request)
c = executor.submit(client.sayHello, request)
d = executor.submit(client.sayHello, request)
e = executor.submit(client.sayHello, request)

print(a)
print(b)
print(c)
print(d)
print(e)
