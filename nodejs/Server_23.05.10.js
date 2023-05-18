var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var path = require('path');
var mysql = require('mysql');
var connection = mysql.createConnection({
	host : 'test-serv.mysql.database.azure.com',
	user : 'rooti',
	password : 'Threego!!',
	database : 'threego'
});

io.on('connection', function(socket){
	console.log('client connected');

	socket.on('message', function(obj){
		console.log('server received data');
		socket.emit('message', 'server received data');
		console.log(obj);
		if(obj == 'showme'){
			connection.connect();
			connection.query('SELECT * FROM STATE', function (error, results, fields){
				socket.emit('message', results)
			});
			connection.end();
		}
	});

	socket.on('disconnect', function(){
		console.log('server disconnected');
	});
});

var PORT = 8080;
http.listen(PORT, function(){
	console.log('listening port : 8080');
});
