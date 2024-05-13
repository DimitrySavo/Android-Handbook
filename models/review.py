
class Review:
    def __init__(self, username, email, text, rating):
        self.username = username
        self.email = email
        self.text = text
        self.rating = rating


    def to_dict(self):
        return self.__dict__