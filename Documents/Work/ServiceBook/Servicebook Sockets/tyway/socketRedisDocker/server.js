var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

//Redis includes
var redis = require('redis');
var redisOptions = {
    host: process.env.REDIS_HOST,
    port: process.env.REDIS_PORT
};

// take LISTEN_PORT var else resolve to PORT 3001
const LISTEN_PORT = process.env.LISTEN_PORT || 3001;

// Listnen to poort 3001
http.listen(LISTEN_PORT, function() {
    console.log("server listening on port %d", http.address().port)
    var pub = redis.createClient(redisOptions);

    io.on('connection', function(socket) {
        console.log("user connected");

        socket.on("notification-channel", function(notificationChannelKey) {
            console.log("Subscribe to notification channel: %s", notificationChannelKey);
            // TODO check notificationChannelKey tobe notification-<32 char key>

            pub.subscribe(notificationChannelKey);

            pub.on("message", function(channel, message) {
                socket.emit('notification', message);
            });
        })

    });
});
