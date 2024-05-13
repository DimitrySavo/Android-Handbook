from bottle import route, template, run, static_file, request
import models.review as reviewClass

@route('/static/<filename>')#route to static files
def static(filename):
    return static_file(filename, root='./views/static')

@route('/static/images/<filename>')#route to images
def getImage(filename):
    return static_file(filename, root='./views/static/images')

topics = {"Тема 1":["firstPage", "secondPage"]}

reviewsList = []
reviewsList.append(reviewClass.Review("!", "email", "review", True))
reviewsList.append(reviewClass.Review("username", "fasfasfas", "r22312eview", False))

@route('/')#route to home page
def home():
    return template('base.tpl', items=topics, topic = template('topics/firstPage.tpl'), title = 'Home')

@route('/topics/<topicName>')#route to topic page
def topic(topicName):
    return template('base.tpl', items=topics, topic = template(f'topics/{topicName}.tpl'),  title = f'{topicName}')

@route('/About')#route to about page
def about():
    return template('about.tpl')

@route('/Contacts')
def contact():
    return template('contact.tpl')

@route('/Reviews')
def reviews():
    return template('reviewsPage.tpl', reviews = reviewsList)

@route('/Твоя страница')# Замени надпись на название твоей страницы. Какое хочешь. Длаьше в base.tpl смотри коммент
def goToNewPage():
    return template('Здесь напиши название своего файла как в других функциях')

@route('/submit', mathode = 'POST')
def submit_review():
    username = request.forms.get('username')
    email = request.forms.get('user-email')
    review = request.forms.get('user-review')
    rating = request.forms.get('rating')

    # Проверка, какая радиокнопка была выбрана
    if rating == 'like':
        rating_value = True
    elif rating == 'dislike':
        rating_value = False

    new_review = reviewClass.Review(username, email, review, rating_value)

    reviewsList.apeend(new_review)


run(host='localhost', port=8080)