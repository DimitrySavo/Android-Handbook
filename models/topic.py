class Topic:
    def __init__(self, title, text, image, url):
        self.title = title
        self.text = text
        self.image = image
        self.url = url

    def to_dict(self):
        return {
            'title': self.title,
            'text': self.text,
            'image': self.image,
            'url': self.url
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['title'], data['text'], data['image'], data['url'])