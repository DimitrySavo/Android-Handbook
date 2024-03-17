from bottle import route, template, run, static_file

@route('/static/<filename>')#route to static files
def static(filename):
    return static_file(filename, root='./views/static')

@route('/static/images/<filename>')#route to images
def getImage(filename):
    return static_file(filename, root='./views/static/images')

topics = {"Тема 1":["firstPage", "secondPage", "подтема 3"], "Тема 2":["подтема 1", "подтема 2", "подтема 3"],"Тема 3":["подтема 1", "подтема 2", "подтема 3"]}


@route('/')#route to home page
def home():
    return template('base.tpl', items=topics, topic = template('topics/firstPage.tpl'), title = 'Home')

@route('/topics/<topicName>')#route to topic page
def topic(topicName):
    return template(f'topics/{topicName}.tpl', items = topics)

@route('/About')#route to about page
def about():
    return template('about.tpl')

run(host='localhost', port=8080)