from bottle import route, template, run, static_file

@route('/static/<filename>')
def static(filename):
    return static_file(filename, root='./views/static')


@route('/')
def home():
    return template('firstPage.tpl')

run(host='localhost', port=8080)