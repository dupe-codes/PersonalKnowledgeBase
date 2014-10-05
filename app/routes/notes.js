'use strict';

// Routes for handling notes

var express = require('express');
var router = express.Router();
var QuickNoteController = require('../controllers/QuickNoteController');
var QuickNote = require('../models/quicknote');

// Create a new quick note
router.post('/', QuickNoteController.addNote);

// Get list of all notes
router.get('/', QuickNoteController.getAllNotes);

// Get page for creating a new note
router.get('/new', function(req, res){
  res.render('newNote');
});

router.get('/list', function(req, res){
  QuickNote.find(function(err, notes) {
    if(err){
      res.send({'success': false, 'err': err});
    } else {
      console.log('Rendering...');
      res.render('noteList', {notes: notes});
    }
  });
});

module.exports = router;
