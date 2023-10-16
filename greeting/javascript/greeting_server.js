const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');

const packageDefinition = protoLoader.loadSync('../../protobufs/greeting.proto', {});
const greetingPackage = grpc.loadPackageDefinition(packageDefinition);


/*
  This is the JS function that we run when we recieve a gRPC call to Greeter.sayHello

  These functions take two parameters: `call` and `callback`
    call: Contains an object which also has the request object containing the values sent from the client.
    callback: A way of returning values to the client.
  */
function sayHello(call, callback) {
  const greeting_message = `Hello, ${call.request.name}!`;

  return callback(null, {greeting: greeting_message});
}

// Create a new gRPC server
const server = new grpc.Server();

// Add the `Greeter` service to this gRPC server.
// You CAN add multiple services to the same gRPC server. This example only uses on service though.
server.addService(
  greetingPackage.Greeter.service,
  {
    // <RPC method name>: <JS function>
    // Greeter.sayHello: greeting_server.js:sayHello
    sayHello: sayHello
  }
);

// Run the gRPC server async and insecurely (without auth or encryption) using the default gRPC port of 50051
server.bindAsync('0.0.0.0:50051', grpc.ServerCredentials.createInsecure(), () => {
  server.start();
});
