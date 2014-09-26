'use strict';

// Routes for handling notes

var express = require('express');
var router = express.Router();
var QuickNoteController = require('../controllers/QuickNoteController');

// Create a new quick note
router.post('/', QuickNoteController.addNote);

// Get list of all notes
router.get('/', QuickNoteController.getAllNotes);

// Get page for creating a new note
router.get('/new', function(req, res){
  res.render('newNote');
});

module.exports = router;
