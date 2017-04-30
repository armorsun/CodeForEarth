var AWS = require('aws-sdk');

function upload(data) {
    AWS.config.update({
        accessKeyId: XXXX,
        secretAccessKey: XXX
    });

    var s3 = new AWS.S3({
        params: {
            Bucket: 'nasaHackathon',
            Key: 'me.jpg', //檔案名稱

            ACL: 'public-read' //檔案權限

        }
    });

    s3.upload({
        Body: data
    }).on('httpUploadProgress', function(evt) {

        //上傳進度

        console.log(evt);
    }).
    send(function(err, data) {
        
        //上傳完畢或是碰到錯誤

    });
}

upload('me.jpg')