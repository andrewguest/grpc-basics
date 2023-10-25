import grpc
from movies_pb2 import AllMoviesRequest
from movies_pb2_grpc import AllMoviesStub

channel = grpc.insecure_channel("localhost:50051")
client = AllMoviesStub(channel)

request = AllMoviesRequest()

all_movies_response = client.get_all_movies(request)

print(all_movies_response)
