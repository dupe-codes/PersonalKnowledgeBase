'use strict';

// Provides logic and services for creating and requesting
// quick notes

var QuickNote = require('../models/quicknote.js');

exports.getAllNotes = function(req, res) {
  QuickNote.find(function(err, notes) {
    if(err) {
      res.send({'success': false, 'error': err});
    } else {
      res.send({'success': true, 'notes': notes});
    }
  });
};

exports.addNote = function(req, res) {
  console.log(req.body);
  var newNote = new QuickNote(req.body);

  newNote.save(function(err) {
    if (err) {
      res.send({'success': false, 'error': err.errors});
    } else {
      res.send({'success': true });
    }
  });
};


