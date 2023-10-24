import asyncio

import grpc
import grpc.experimental.aio
from movies_pb2 import AllMoviesResponse, MovieEntry
from movies_pb2_grpc import AllMoviesServicer, add_AllMoviesServicer_to_server


class AsyncMoviesService(AllMoviesServicer):
    async def get_all_movies(self, request, context):
        all_movies = [
            MovieEntry(title="Movie title #1")
        ]

        return AllMoviesResponse(movies=all_movies)


async def main():
    server_port = 50051

    grpc.experimental.aio.init_grpc_aio()

    # Create the async gRPC server
    server = grpc.experimental.aio.server()
    server.add_insecure_port(f"[::]:{server_port}")
    print(f"Server listening on: 0.0.0.0:{server_port}")

    add_AllMoviesServicer_to_server(AsyncMoviesService(), server)

    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.run(main())
