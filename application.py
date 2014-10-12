#!/usr/local/Cellar/python/2.7.6/bin/python

import yaml

from flask import Flask
from flask import make_response
from flask import request
from jinja2 import Environment
from jinja2 import PackageLoader
from jinja2 import Template
from sqlalchemy import create_engine
from sqlalchemy.sql import select
from sqlalchemy.sql import table, column, func, join, literal_column

from lib import Data
from lib import Api

app = Flask(__name__)
env = Environment(loader=PackageLoader('application', 'templates'))
db = create_engine('mysql://login:password@host/db')

def render_template(template_path):
    return make_response(open("templates/" + template_path).read())

def getCourseById(id):
    course = table('course', column('id'), column('title'), column('description'), column('alias'))
    s = select([course]).where(course.c.id == id)
    result = db.execute(s)
    return result.fetchone()

def getVideoByCourseId(courseId):
        video = table('video', 
                column('id'), 
                column('video_url'), 
                literal_column('video.video_id').label('external_id'), 
                column('type'))
        videoCourse = table('course_video',  
                column('video_id'), 
                column('course_id'), 
                column('video_order'),
                column('video_title'))
        join1 = join(video, videoCourse, video.c.id == videoCourse.c.video_id)
        s = select([
                video.c.type, 
                video.c.video_url, 
                video.c.external_id, 
                videoCourse.c.video_order, 
                videoCourse.c.video_title
            ]).select_from(join1).where(videoCourse.c.course_id == courseId)

        result = db.execute(s)
        row = result.fetchall()
        res = []
        for i in row:
            res.append(dict(i))

        return row

@app.route('/')
def index():
    courses = Api.Api().getCourses()
    template = env.get_template("index.html")
    return template.render(courses=courses)

@app.route('/courses/')
def coursesDetails():
    courses = Api.Api().getCourses()
    template = env.get_template("courses.html")
    return template.render(courses=courses)

@app.route('/course/<courseAlias>')
def getCourse(courseAlias):
    course = Api.Api().getCourse(courseAlias)
    template = env.get_template("course.html")
    return template.render(course=course)

@app.route('/course/<courseAlias>/video/<videoAlias>')
def getVideo(courseAlias, videoAlias):
    video = Api.Api().getVideoByAlias(courseAlias, videoAlias)
    template = env.get_template("screencast.html")
    return template.render(video=video)

@app.route('/categories/<tagname>')
def showTags(tagname):
    courses = Data.getCoursesByTagname(tagname)
    template = env.get_template("categories.html")
    return template.render(category=tagname, courses=courses)

@app.route('/channels/')
def getChannels():
    channels = Data.getChannels()
    template = env.get_template("channels.html")
    return template.render(channels=channels)

@app.route('/get-course/<courseAlias>')
def getCourseJsonp(courseAlias):
    course = Api.Api().getCourse(courseAlias)
    content = request.args.get('callback') + '(' + str(course) + ')'
    return app.response_class(content, mimetype='application/javascript')


@app.route('/test-course/')
def getTestVideo():
    courseResult = dict(getCourseById(1))
    videoResult = getVideoByCourseId(1)
    template = env.get_template("screencast_test.html")
    courseResult['videos'] = videoResult
    return template.render(course=courseResult)

@app.route('/get-data-from/')
def getCourseJsonpDB():
    course = table('course', column('id'), column('title'), column('description'), column('alias'))
    video = table('video', column('id'), column('video_url'), literal_column('video.video_id').label('external_id'), column('type'))
    videoCourse = table('course_video',  
            column('video_id'), 
            column('course_id'), 
            column('video_order'),
            column('video_title'))

    courseResult = dict(getCourseById(1))
    
    videoResult = getVideoByCourseId(1)
    return app.response_class(str(dict(course=courseResult, videos=videoResult)), mimetype='application/json')

if __name__ == "__main__":
    app.run(debug=True)