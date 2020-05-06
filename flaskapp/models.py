
from datetime import datetime
from flaskapp import db
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(20), default="Admin")
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.String(1000), nullable= False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    def __repr__(self):
        return f'Post: Id:{self.id}, Author:{self.author}, Title={self.title}'

