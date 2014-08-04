#!/usr/local/Cellar/python/2.7.6/bin/python

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
@app.route('/show-courses/')
@app.route('/courses/')
def coursesDetails():
    courses = Data.getCourses()
    template = env.get_template("index.html")
    return  template.render(courses=courses)

@app.route('/show-videos/')
def videoDetails():
    template = env.get_template("video_details.html")
    return template.render(videos={})

@app.route('/categories/<tagname>')
def showTags(tagname):
    courses = Data.getCoursesByTagname(tagname)
    template = env.get_template("categories.html")
    return  template.render(category=tagname, courses=courses)

#app.register_blueprint(Api)

if __name__ == "__main__":
    app.run(debug=True)