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

	socket.on('error', function(e){
		console.log(e);
	})

	socket.on('update', function(data){
		var name = data.name;
		var state = data.state;
		connection.query('UPDATE STATE SET STATE = ? WHERE NAME = ?;', [state, name], function(err, result, fields) {
			if(err){
			  console.log(err);
			}
		});
		connection.query('SELECT * FROM STATE;', function (error, results, fields){
			io.emit('response_data', results)
		});
	});

	socket.on('request_data', function(){
		console.log('Client request data');	
		
		connection.query('SELECT * FROM STATE;', function (error, results, fields){
			socket.emit('response_data', results)
		});
		
	});

	socket.on('disconnect', function(){
		console.log('server disconnected');

		
	});
});

var PORT = 8080;
http.listen(PORT, function(){
	console.log('listening port : 8080');
});
