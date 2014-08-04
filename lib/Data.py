import yaml

def getVideoByAlias(courseAlias, videoAlias):
    course = getCourseByAlias(courseAlias)
    return filter(lambda x: videoAlias == x['alias'], course['videos'])[0] 

def getChannels():
    channels = []
    f = open('data/channels.yml', 'r')
    channelsDict = yaml.load(f)
    for name, channel in channelsDict.iteritems():
        channel['id'] = name
        channels.append(channel)
    return channels

def getCourses():
    courses = []
    f = open('data/screencasts.yml', 'r')
    screencasts = yaml.load(f)
    for name, screencast in screencasts.iteritems():
        screencast['id'] = name
        courses.append(screencast)
    return courses

def getCourseByAlias(alias):
    courses = []
    f = open('data/screencasts.yml', 'r')
    screencasts = yaml.load(f)
    for name, screencast in screencasts.iteritems():
        if alias == screencast['alias']:
            return screencast

def getCoursesByTagname(tagname):
    return filter(lambda x: tagname in x['tags'], getCourses())