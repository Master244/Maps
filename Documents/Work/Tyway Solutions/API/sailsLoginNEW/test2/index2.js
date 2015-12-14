// var socketIOClient = require('socket.io-client');
// var sailsIOClient = require('sails.io.js');

// // Instantiate the socket client (`io`)
// // (for now, you must explicitly pass in the socket.io client when using this library from Node.js)
// var io = sailsIOClient(socketIOClient);

// // Set some options:
// // (you have to specify the host and port of the Sails backend when using this library from Node.js)
// io.sails.url = 'http://localhost:1337';
// // ...

// // Send a GET request to `http://localhost:1337/hello`:
// io.socket.get('/hello', function serverResponded (body, JWR) {
//   // body === JWR.body
//   console.log('Sails responded with: ', body);
//   console.log('with headers: ', JWR.headers);
//   console.log('and with status code: ', JWR.statusCode);

  // When you are finished with `io.socket`, or any other sockets you connect manually,
  // you should make sure and disconnect them, e.g.:
  //io.socket.disconnect();

  // (note that there is no callback argument to the `.disconnect` method)
//});

// var tempObj = {
//   loggername: 'loggername',
//   loggerID: 'test'
// }


// io.socket.get('/LoggerHandshake', tempObj, function serverResponded (body, JWR) {
// //all we're doing now is subscribing to a room
//     var session = body;
//     console.dir('dit is die sessions van handshake' + session)
// });

// io.socket.on('anevent',function(message){
//     var messageRespons = message;
//     console.dir(messageRespons)
// });





setInterval(function () {
  setTimeout(f, 4000)
}, 1000);



function f() {
  var http = require('http'),
    queryString = require('querystring');
  // var final = { Logger: []}
  var random = parseInt((Math.random() * 10))
  // final.Logger = 'laatste'
  // final.Logger.temp = {tempf: random, tempc: '4', measuredAt: 'iets', logger:'jeweet'}
var postData = JSON.stringify({
  'ownerID': '566e10fffa42bbee136998fe',
  'logger' : '566e111cfa42bbee13699900',
  'tempf' : '8',
  'tempc' : random
});

var options = {
  hostname: 'localhost',
  port: 1337,
  path: '/temp/create',
  method: 'POST',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': postData.length
  }
};

var req = http.request(options, function(res) {
  console.log('STATUS: ' + res.statusCode);
  console.log('HEADERS: ' + JSON.stringify(res.headers));
  res.setEncoding('utf8');
  res.on('data', function (chunk) {
    console.log('BODY: ' + chunk);
  });
  res.on('end', function() {
    console.log('No more data in response.')
  })
});

req.on('error', function(e) {
  console.log('problem with request: ' + e.message);
});

// write data to request body
req.write(postData);
req.end();
}
