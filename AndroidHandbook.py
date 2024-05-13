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

    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            reviewsList = json.load(file)
    else:
        reviewsList = []

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

    
    if not rating:
        return#TODO
    
    if not VH.Validation.ValidateEmail(email):
        return#TODO
    
    if not VH.Validation.ValidateUserName(username):
        return#TODO

    new_review = reviewClass.Review(username, email, review, rating_value)

    reviewsList = []

    

    reviewsList.append(new_review)

    with open(FILE_PATH, "w") as file:
        reviewsList_dict = [review.to_dict() for review in reviewsList]
        json.dump(reviewsList_dict, file)
    
    
    


run(host='localhost', port=8080)