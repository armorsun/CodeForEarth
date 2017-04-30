//  var params = {
//   Image: {
//    S3Object: {
//     Bucket: "nasaHackathon", 
//     Name: "me.jpg"
//    }
//   }
//  };

// var AWS = require('aws-sdk');
// AWS.config.update({accessKeyId: 'AKIAIQSFHOYQG4PKBBYA', secretAccessKey: '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', region: 'us-east-1'});


// var rekognition = new AWS.Rekognition();


// rekognition.detectFaces(params, function(err, data) {
//    if (err) console.log(err, err.stack); // an error occurred
//    else     console.log(data); console.log(data.FaceDetails[0])          // successful response
// });

 var params = {
  Image: {
   S3Object: {
    Bucket: "nasaHackathon", 
    Name: "pic/frame.jpg"
   }
  }, 
  MaxLabels: 123, 
  MinConfidence: 70
 };
 var AWS = require('aws-sdk');
 AWS.config.update({accessKeyId: XXX, secretAccessKey: XXX, region: 'us-east-1'});
var rekognition = new AWS.Rekognition();


 rekognition.detectLabels(params, function(err, data) {
   if (err) console.log(err, err.stack); // an error occurred
   else     console.log(data);       
});
 