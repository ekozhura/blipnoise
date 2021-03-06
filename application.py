#!/usr/local/Cellar/python/2.7.6/bin/python

import yaml

from flask import Flask
from flask import make_response
from jinja2 import Environment
from jinja2 import PackageLoader
from jinja2 import Template

from lib import Data

app = Flask(__name__)
env = Environment(loader=PackageLoader('application', 'templates'))

def render_template(template_path):
    return make_response(open("templates/" + template_path).read())

@app.route('/')
def index():
    courses = Data.getCourses()
    template = env.get_template("index.html")
    return  template.render(courses=courses)

@app.route('/courses/')
def coursesDetails():
    courses = Data.getCourses()
    template = env.get_template("courses.html")
    return  template.render(courses=courses)

@app.route('/course/<courseAlias>')
def getCourse(courseAlias):
    course = Data.getCourseByAlias(courseAlias)
    template = env.get_template("course.html")
    return  template.render(course=course)

@app.route('/course/<courseAlias>/video/<videoAlias>')
def getVideo(courseAlias, videoAlias):
    video = Data.getVideoByAlias(courseAlias, videoAlias)
    template = env.get_template("screencast.html")
    return template.render(video=video)

@app.route('/categories/<tagname>')
def showTags(tagname):
    courses = Data.getCoursesByTagname(tagname)
    template = env.get_template("categories.html")
    return  template.render(category=tagname, courses=courses)

@app.route('/channels/')
def getChannels():
    channels = Data.getChannels()
    template = env.get_template("channels.html")
    return  template.render(channels=channels)

#app.register_blueprint(Api)

if __name__ == "__main__":
    app.run(debug=True)