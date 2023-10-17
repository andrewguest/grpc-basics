// Imports
const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');

const packageDefinition = protoLoader.loadSync('../protobufs/recommendations.proto', {});
const recommendationPackage = grpc.loadPackageDefinition(packageDefinition).recommendations;


const server = new grpc.Server();

server.addService(recommendationPackage, {
  Recommendations: Recommendations
});

server.bindAsync('0.0.0.0:50051', grpc.ServerCredentials.createInsecure(), () => {
  console.log("Server running at http://127.0.0.1:50051");
  server.start();
});


// Mock database query and queryset



function Recommendations(call, callback) {
  const user_id = call.request.user_id;
  const category = call.request.category;
  const max_results = call.request.max_results;

  callback(null, { 'id': 3, 'title': 'From the Javascript server' });
};
