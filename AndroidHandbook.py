from bottle import route, template, run, static_file

@route('/static/<filename>')
def static(filename):
    return static_file(filename, root='./views/static')

topics = {"Тема 1":["firstPage", "secondPage", "подтема 3"], "Тема 2":["подтема 1", "подтема 2", "подтема 3"],"Тема 3":["подтема 1", "подтема 2", "подтема 3"]}


@route('/')
def home():
    return template('base.tpl', items=topics, topic = template('topics/firstPage.tpl'), title = 'Home')

@route('/topics/<topicName>')
def topic(topicName):
    return template(f'topics/{topicName}.tpl', items = topics)

@route('/About')
def about():
    return template('about.tpl')

run(host='localhost', port=8080)    