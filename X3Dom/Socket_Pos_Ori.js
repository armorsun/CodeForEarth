var socket = io.connect('http://ec2-54-204-81-60.compute-1.amazonaws.com:3579/'); // 連線至伺服器
console.log("Connected to EC2? ", socket.connected);
console.log(socket);

socket.on('socketToWeb', function (data) {
  reveivedObj = data;
  console.log(reveivedObj);
});
