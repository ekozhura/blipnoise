from lib import Data

class Api:
    def __init__(self):
        return None

    def getVideos(self):
        return []

    def getVideo(self, course, video):
        video = Data.getVideoByAlias(course, video)
        return video

    def getCourses(self):
        return Data.getCourses()

    def getCourse(self, courseAlias):
        course = Data.getCourseByAlias(courseAlias)
        return course

    def getArticles(self):
        return []

    def addVideo(self):
        return False

    def addCourse(self):
        return False

    def addArticle(self):
        return False