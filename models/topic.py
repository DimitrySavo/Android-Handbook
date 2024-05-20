class Topic:
    def __init__(self, title, text, image, url, date, telephoneNumber):
        self.title = title #Заголовок
        self.text = text #Основной текст
        self.image = image #Картинка
        self.url = url #Ссылка
        self.date = date #Дата
        self.telephoneNumer = telephoneNumber #Телефонный номер

    def to_dict(self): #Превращение текущего объекта в словарь
        return {
            'title': self.title,
            'text': self.text,
            'image': self.image,
            'url': self.url,
            'date': self.date,
            'telephoneNumber': self.telephoneNumer
        }
    
    @classmethod
    def from_dict(cls, data): #Получить текущий объект из словаря
        return cls(data['title'], data['text'], data['image'], data['url'], data['date'], data['telephoneNumber'])