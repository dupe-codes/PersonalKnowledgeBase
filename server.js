'use strict';

/*
 * Simple app to serve up my personal knowledgebase
 * on the web.
 */

 var express = require('express');

 var app = express();


/* Render table of contents when home page requested */
// TODO: Add ability to request specific pages, maybe include path in request?
app.get('/', function(req, res) {
    res.sendFile('./Rendered/index.html');
});

 // Basic error handling
 app.use(function(req, res, next) {
    var err = new Error('Not Found');
    err.status = 404;
    next(err);
});

app.use(function(err, req, res, next) {
    res.status(err.status || 500);
    res.send('A ' + err.status + ' error occured');
});

var port = process.env.PORT || 8080;
app.listen(port)
console.log('Server started on port ' + port);
