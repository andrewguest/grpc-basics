const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');

const packageDefinition = protoLoader.loadSync('../../protobufs/movies.proto', {});
const moviesPackage = grpc.loadPackageDefinition(packageDefinition);


function get_all_movies(call, callback) {
  let all_movies = [
    { title: "From Javascript" }
  ]

  return callback(null, {movies: all_movies});
}

// Create a new gRPC server
const server = new grpc.Server();

server.addService(
  moviesPackage.AllMovies.service,
  {
    get_all_movies: get_all_movies
  }
);

// Run the gRPC server async and insecurely (without auth or encryption) using the default gRPC port of 50051
server.bindAsync('0.0.0.0:50051', grpc.ServerCredentials.createInsecure(), () => {
  server.start();
});
