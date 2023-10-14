import grpc

from recommendations_pb2 import BookCategory, RecommendationRequest
from recommendations_pb2_grpc import  RecommendationsStub


channel = grpc.insecure_channel("localhost:50051")
client = RecommendationsStub(channel)
request = RecommendationRequest(
    user_id = 1,
    category = BookCategory.SELF_HELP,
    max_results = 2
)

recommendations = client.Recommend(request)

print(recommendations)
