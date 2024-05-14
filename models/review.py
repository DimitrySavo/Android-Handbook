
class Review:
    def __init__(self, username, email, text, rating):
        self.username = username
        self.email = email
        self.text = text
        self.rating = rating


    def to_dict(self):
        return {
            'username': self.username,
            'email': self.email,
            'text': self.text,
            'rating': self.rating
        }
    
    @classmethod
    def from_dict(cls, review_dict):
        return cls(review_dict['username'], review_dict['email'], review_dict['text'], review_dict['rating'])