var fs = require('fs');

var dataStore = {};

var _openStore = function(fn) {
  fs.readFile(__dirname + "/../data/screencasts.json", fn);
};

dataStore.getCourses = function(fn) {
  _openStore(function(err, data){
    var courses = JSON.parse(data);

    for (course in courses) {
      if(courses.hasOwnProperty(course)) {
        courses[course].id = course;
      }
    }
    fn(courses);
  });
};

dataStore.getCourseByAlias = function(alias, fn) {
  _openStore(function(err, data){
    var courses = JSON.parse(data);
    for (course in courses) {
      if(courses.hasOwnProperty(course) && courses[course].alias === alias) {
        courses[course]["id"] = course;
        return fn(courses[course]);
      }
    }
  });
};

module.exports = dataStore;
