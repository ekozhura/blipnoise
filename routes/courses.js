var express = require('express');
var router = express.Router();

var dataStore = require('./../lib/datastore');

router.get('/', function(req, res, next) {
  dataStore.getCourses(
    function(courses) {
      res.render('courses', { courses: courses });
    }
  );
});


router.get('/:courseAlias', function(req, res, next){
  var alias = req.params.courseAlias;
  dataStore.getCourseByAlias(
    alias,
    function(courses) {
      res.render('course', { title: alias});
    }
  );
});

module.exports = router;
