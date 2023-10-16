import random
from concurrent import futures

import grpc

from recommendations_pb2 import (
    BookCategory,
    BookRecommendation,
    RecommendationResponse,
)
import recommendations_pb2_grpc


# Mock database query and queryset
books_by_category = {
    BookCategory.MYSTERY: [
        BookRecommendation(id=1, title="The Maltese Falcon"),
        BookRecommendation(id=2, title="Murder on the Orient Express"),
        BookRecommendation(id=3, title="The Hound of the Baskervilles"),
    ],
    BookCategory.SCIENCE_FICTION: [
        BookRecommendation(
            id=4, title="The Hitchhiker's Guide to the Galaxy"
        ),
        BookRecommendation(id=5, title="Ender's Game"),
        BookRecommendation(id=6, title="The Dune Chronicles"),
    ],
    BookCategory.SELF_HELP: [
        BookRecommendation(
            id=7, title="The 7 Habits of Highly Effective People"
        ),
        BookRecommendation(
            id=8, title="How to Win Friends and Influence People"
        ),
        BookRecommendation(id=9, title="Man's Search for Meaning"),
    ],
}

# Defines the RecommendationService class.
# This is the implementation of your microservice. Note that you subclass RecommendationsServicer.
# This is part of the integration with gRPC that you need to do.
class RecommendationService(recommendations_pb2_grpc.RecommendationsServicer):

    # Defines a Recommend() method on the class.
    # This must have the same name as the RPC you define in your protobuf file. It also takes a RecommendationRequest and returns a RecommendationResponse just like in the protobuf definition. It also takes a context parameter.
    # The context allows you to set the status code for the response.
    def Recommend(self, request, context):
        if request.category not in books_by_category:
            # Use abort() to end the request and set the status code to `NOT_FOUND` if you get an unexpected category.
            context.abort(grpc.StatusCode.NOT_FOUND, "Category not found")

        # Randomly pick some books from the given category to recommend.
        books_for_category = books_by_category[request.category]
        num_results = min(request.max_results, len(books_for_category))
        books_to_recommend = random.sample(books_for_category, num_results)

        return RecommendationResponse(recommendations=books_to_recommend)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    recommendations_pb2_grpc.add_RecommendationsServicer_to_server(
        RecommendationService(),
        server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
