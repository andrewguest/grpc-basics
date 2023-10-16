import asyncio

import grpc
import grpc.experimental.aio
from greeting_pb2 import GreetingResponse
from greeting_pb2_grpc import GreeterServicer, add_GreeterServicer_to_server


class AsyncGreeterService(GreeterServicer):
    def __init__(self):
        self.TOTAL_REQUESTS_RECEIVED = 0

    async def sayHello(self, request, context):
        self.TOTAL_REQUESTS_RECEIVED += 1
        print(f"Message: {self.TOTAL_REQUESTS_RECEIVED}")

        greeting_message = f"Hello, {request.name}!"

        return GreetingResponse(greeting=greeting_message)


async def main():
    grpc.experimental.aio.init_grpc_aio()

    # Create an async gRPC server
    server = grpc.experimental.aio.server()
    server.add_insecure_port("[::]:50051")
    print("Server listening on: 0.0.0.0:50051")

    add_GreeterServicer_to_server(
        AsyncGreeterService(),
        server
    )

    await server.start()
    await server.wait_for_termination()


asyncio.run(main())
