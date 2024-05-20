from bottle import route, template, run, static_file, request, post, response
import models.review as reviewClass
import models.ValidationHelper as VH
import os
import json
from datetime import datetime

# Функция для загрузки карточек из JSON файла
def load_news_cards(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return []

# Мы создаем список карточек новостей
news_cards = load_news_cards("news_cards.json")

# Функция для сохранения карточек в JSON файл
def save_news_cards(file_path):
    with open(file_path, "w") as file:
        json.dump(news_cards, file)

# Функция для проверки URL
def is_valid_url(url):
    # Здесь можно добавить более строгие проверки
    return url.startswith('http://') or url.startswith('https://')

# Функция для проверки URL
def is_valid_data(data):
    # Здесь можно добавить более строгие проверки
    return VH.Validation.ValidateDate(data)

@route('/')  # Главная страница
def index():
    return open('index.html').read()

@route('/submit', method='POST')  # Обработка отправленной формы для добавления новой карточки
def submit():
    title = request.forms.get('title')
    description = request.forms.get('description')
    image_url = request.forms.get('image_url')
    link = request.forms.get('link')
    date = request.forms.get('date')
    
    # Проверка корректности введенных данных
    if not (title and description and image_url and link):
        return json.dumps({"error": "Все поля должны быть заполнены"})
    elif not is_valid_url(image_url) or not is_valid_url(link):
        return json.dumps({"error": "Некорректный URL"})
    elif not VH.Validation.ValidateDate(date):
        return json.dumps({"error": "Некорректная Дата"})
    else: 
        new_card = {"title": title, "description": description, "image_url": image_url, "link": link, "date": date}
        # Добавляем карточку в список карточек
        news_cards.append(new_card)

        # Сохраняем обновленный список карточек в JSON файл
        save_news_cards("news_cards.json")
        
        # Возвращаем данные о добавленной карточке в формате JSON
        response.content_type = 'application.json'
        return json.dumps(new_card)


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

@route('/CurrentNews')# Замени надпись на название твоей страницы. Какое хочешь. Длаьше в base.tpl смотри коммент
def goToNewPage():
    news_cards = load_news_cards("news_cards.json")
    submit()
    return template('currentNews.tpl', news_cards=news_cards)


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

    new_review = reviewClass.Review(username, email, review, rating_value, datetime.now())

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