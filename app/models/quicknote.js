'use strict';

// Defines the model for storing quick notes

var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var noteSchema = new Schema({
  title: {
    type: String,
    default: '',
    required: 'Note title must be provided'
  },
  content: {
    type: String,
    default: '',
    required: 'Note content must be provided'
  },
  category: {
    type: String,
    default: 'QuickNote'
  },
  created: {
   type: Date,
   default: Date.now
  }
});

module.exports = mongoose.model('QuickNote', noteSchema);
