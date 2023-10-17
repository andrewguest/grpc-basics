# Methods of commmunication

### Unary RPC
Here, a client makes a request to the server and waits synchronously for a response. The server on the other hand does what it has to do; database query or computation or a call to another service.

```proto
rpc Greet(HelloRequest) returns (HelloResponse);
```

### Server streaming RPC
The client here sends a stream of messages or data continuously to the server. The server waits for the client to send all messages before it acknowledges and sends a response. For example, uploading a large file to the server will better be implemented using a stream to send chunks of the messages to the particular service.

```proto
rpc Greetings(HelloRequest) returns (stream HelloResponses);
```

### Client streaming RPC
The client here sends a stream of messages or data continuously to the server. The server waits for the client to send all messages before it acknowledges and sends a response. For example, uploading a large file to the server will better be implemented using a stream to send chunks of the messages to the particular service.

```proto
rpc Greetings(stream HelloRequests) returns (HelloResponse);
```


### Bidirectional steaming RPC
A combination of server and client streaming where both the server and client can send a stream of messages to each other. Both the client and server communicate independently. And the client can asynchronously send a stream of messages while the server is sending. An example of this is chatting, gaming, and so on.

```proto
rpc Greetings(stream HelloRequests) returns (stream HelloResponses);
```

---

# How to write Protobuf files

1) Create a file with a `.proto` extension


2) At the top of the new file add this line to use **proto3** syntax instead of the default **proto2** syntax
    ```proto
        syntax = "proto3";
    ```


3) Define a couple of Protobuf `message`s
   1) These define the structure of the incoming and outgoing messages exchanged between the two servers.
   2) `<field data type>` `<field name>` = `<field number>`
      1) The `<field number>` cannot be repurposed or reused within a `message` definition. If a field is deleted then it's number should be reserved and NOT reused.
      2) From a compatibility perspective, unique field numbers are the most vital piece of the message declaration. These numbers (the = 1 after the name declaration) are used as identifiers for fields after they are converted to binary. When the message is decoded, a crucial step for compatibility is allowing the parser to skip fields it doesn’t recognize so it’s possible to add new fields without breaking programs that weren’t designed to look for them.
      3) The unique field number is combined with a wire type corresponding to the data type of the field. This identifier and type combination form the key of every field in a message. These fields combined give the receiver the ability to uniquely identify fields and determine the length of the field, so it knows when to start looking for the next field.
      4) This means once a unique field number or length is set, it cannot be changed. Any program consuming or serializing protobuf data needs the number to be fixed forever, or both the sender and all the receivers must be updated.

    ```proto
        // Incoming request
        message PersonRequest {
            string name = 1;
            int32 age = 2;
        }

        // Outgoing response
        message PersonResponse {
            string message = 1;
        }
    ```


4) Define a Protobuf `service`
    1) A service defines what data type(s) the RPC server should look for and what data type(s) the RPC client should expect in return.

    ```proto
        service Greeter {
            rpc SayHello (PersonRequest) returns (PersonResponse) {}
        }
    ```

---

# How to compile `.proto` files to Python code
1) Install the async `grpclib` package:

```
pip install "grpclib[protobuf]"
```

2) Compile the `.proto` file to 2 `.py` files:

```
python -m grpc_tools.protoc -I <directory to search for imports in> --python_out=<directory to write output .py files to> --grpc_python_out=<directory to write output .py files to> <.proto file(s) to compile>
```

Example:
```
python -m grpc_tools.protoc -I ./protobufs --python_out=./python --grpc_python_out=./python ./protobufs/recommendations.proto
```
