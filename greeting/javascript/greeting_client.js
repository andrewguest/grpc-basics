const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');

const packageDefinition = protoLoader.loadSync('../../protobufs/greeting.proto', {});
const greetingPackage = grpc.loadPackageDefinition(packageDefinition);


const client = new greetingPackage.Greeter(
  // gRPC server to connect to
  'localhost:50051',

  // Use insecure mode
  grpc.credentials.createInsecure()
);

// Call the `sayHello` RPC method on the server
// {'name': 'Jason Bourne'} is the request body
client.sayHello({'name': 'Jason Bourne'}, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`From server`, JSON.stringify(response));
  }
});
