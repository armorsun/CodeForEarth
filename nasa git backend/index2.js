// const express = require('express')
// const app = express()
// app.get('/', (req, res) => {
//   res.send('HEY!')
// })
// app.listen(3579, () => console.log('Server running on port 3579'))

var app = require('express')();
var server = require('http').Server(app);
var io = require('socket.io')(server);

server.listen(3579);

app.get('/', function (req, res) {
  res.send('HEY!')
});

io.on('connection', function (socket) {
	console.log('連線成功');
  socket.on('intelToSocket', function (data) {
    console.log('傳送socket給web');
    socket.emit('socketToWeb', data);
	    console.log(data);
	  });
    socket.broadcast.emit('socketToWeb', data); // 廣播
});
      
