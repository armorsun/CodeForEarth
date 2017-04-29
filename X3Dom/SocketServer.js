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

var data = {
	"seq": 0.0001,
	"pos1": 0.0001,
	"pos2": 0.0001,
	"pos3": 0.0,
	"ori1": 0.0001,
	"ori2": 0.0001,
	"ori3": 0.0001,
	"ori4": 0.0001,
	}

app.get('/', function (req, res) {
  res.send('HEY!')
});

io.on('connection', function (socket) {
	console.log('連線成功', socket.id);

	setInterval(function(){
		data.pos3 += 0.01;
		socket.emit('socketToWeb', data);
	},100);
	
});
      
