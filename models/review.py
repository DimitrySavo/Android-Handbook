from datetime import datetime
class Review:
    def __init__(self, username, email, text, rating, dateCreate):
        self.username = username
        self.email = email
        self.text = text
        self.rating = rating
        self.dateCreate = dateCreate.isoformat()  # Convert datetime to string


    def to_dict(self):
        return {
            'username': self.username,
            'email': self.email,
            'text': self.text,
            'rating': self.rating,
            'dateCreate': self.dateCreate
        }
    
    @classmethod
    def from_dict(cls, review_dict):
        return cls(review_dict['username'], review_dict['email'], review_dict['text'], review_dict['rating'],datetime.strptime(review_dict['dateCreate'], '%Y-%m-%dT%H:%M:%S.%f'))