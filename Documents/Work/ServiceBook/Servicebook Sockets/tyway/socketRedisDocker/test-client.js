var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

//Redis includes
var redis = require('redis');
var redisOptions = {
    host: process.env.REDIS_HOST,
    port: process.env.REDIS_PORT
};

// PUB/SUB/SUBSCRIBE setup
var pub = redis.createClient(redisOptions);

setInterval(function() {
    pub.publish("notification-1", new Date().getTime());
}, 1000);

http.listen(8000, function() {
    // Serve index.html
    app.get('/', function(req, res){
        //send the index.html file for all requests
        res.sendFile(__dirname + '/index.html');
    });

})
