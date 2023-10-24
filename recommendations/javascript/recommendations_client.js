// Imports
const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');

const packageDefinition = protoLoader.loadSync('../../protobufs/recommendations.proto', {});
const recommendationPackage = grpc.loadPackageDefinition(packageDefinition).recommendations;

const client = new recommendationPackage.Recommendations('localhost:50051', grpc.credentials.createInsecure());

client.Recommend(
  {
    'user_id': 12345,
    'category': recommendationPackage.BookCategory.SELF_HELP,
    'max_results': 5
  },
  (err, response) => {
    if (err) {
      console.log(err);
    } else {
      console.log('From server', JSON.stringify(response));
    }
  }
);
