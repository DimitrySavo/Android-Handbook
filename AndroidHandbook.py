from bottle import route, template, run, static_file, request, post
import models.review as reviewClass
import models.ValidationHelper as VH
import os
import json

@route('/static/<filename>')#route to static files
def static(filename):
    return static_file(filename, root='./views/static')

@route('/static/images/<filename>')#route to images
def getImage(filename):
    return static_file(filename, root='./views/static/images')

topics = {"Тема 1":["firstPage", "secondPage"]}

FILE_PATH = "reviews.json"

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
    reviewsList = load_reviews(FILE_PATH)
    return template('reviewsPage.tpl', reviews = reviewsList)

@route('/Твоя страница')# Замени надпись на название твоей страницы. Какое хочешь. Длаьше в base.tpl смотри коммент
def goToNewPage():
    return template('Здесь напиши название своего файла как в других функциях')

@route('/submit_review', method='POST')
def submit_review():
    username = request.forms.get('username')
    email = request.forms.get('user-email')
    review = request.forms.get('user-review')
    rating = request.forms.get('rating')


    # Проверка, какая радиокнопка была выбрана
    if rating == 'like':
        rating_value = True
    else:
        rating_value = False
    
    if not VH.Validation.ValidateEmail(email):
        return "Неверный формат почты"
    
    if not VH.Validation.ValidateUserName(username):
        return "Неверное имя пользователя"

    new_review = reviewClass.Review(username, email, review, rating_value)

    reviewsList = load_reviews(FILE_PATH)

    for review in reviewsList:
        if new_review.email == review.email:
            reviewsList.remove(review)
        elif new_review.username == review.username:
            return "Этот логин уже существует"

    reviewsList.append(new_review)


    with open(FILE_PATH, "w") as file:
        reviewsList_dict = [review.to_dict() for review in reviewsList]
        json.dump(reviewsList_dict, file)
    
    
    
def load_reviews(file_path):
    reviews = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            reviewsList_dict = json.load(file)
            for review_dict in reviewsList_dict:
                reviews.append(reviewClass.Review.from_dict(review_dict))
    return reviews

run(host='localhost', port=8080)