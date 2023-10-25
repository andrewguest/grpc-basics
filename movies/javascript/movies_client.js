const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');

const packageDefinition = protoLoader.loadSync('../../protobufs/movies.proto', {});
const moviesPackage = grpc.loadPackageDefinition(packageDefinition);


const client = new moviesPackage.AllMovies(
  // gRPC server to connect to
  'localhost:50051',

  // Use insecure mode
  grpc.credentials.createInsecure()
);

client.get_all_movies({}, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`From server`, JSON.stringify(response));
  }
});
