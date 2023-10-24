import grpc

from recommendations_pb2 import BookCategory, RecommendationRequest
from recommendations_pb2_grpc import  RecommendationsStub


# Create an insecure connectioin to the default gRPC port of 50051 on localhost
# "insecure" means it's unauthenticated and unencrypted
channel = grpc.insecure_channel("localhost:50051")

# Instantiate the client by passing the channel to the stub
client = RecommendationsStub(channel)

# Create an instance of RecommendationRequest
request = RecommendationRequest(
    user_id = 1,
    category = BookCategory.SELF_HELP,
    max_results = 2
)

# Call the Recommend method of the Recommendations microservice and pass the RecommendationRequest
#   body created above
recommendations = client.Recommend(request)

# Print the response from the Recommend() method
print(recommendations)
