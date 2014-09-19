'use strict';

/*
 * Simple app to serve up my personal knowledgebase
 * on the web.
 */

 var express = require('express');
 var path = require('path');

 var app = express();
 app.set('showStackError', true);

// Expose all rendered files to top-level domain
app.use(express.static(path.join(__dirname, './Rendered/')));

/* Render table of contents when home page requested */
// TODO: Add ability to request specific pages, maybe include path in request?
app.get('/', function(req, res) {
    res.sendFile(path.resolve('./Rendered/index.html'));
});

app.get('/errorlog', function(req, res) {
  res.send('Error logging will appear here');
  // TODO: Figure out best way to handle logging on heroku app
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
