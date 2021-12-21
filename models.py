"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()
def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    '''user'''
    __tablesname__ = 'Users'

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(15), nullable = False)
    last_name = db.Column(db.String(15), nullable = False)
    img_url = db.Column(db.String(1000), nullable = False)
    
    
    

    def name(self):
        return f'{self.first_name} {self.last_name}'

class Post(db.Model):
    '''posts'''
    __tablename__ = 'Posts'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(20), nullable = False)
    content = db.Column(db.String(500), nullable = False)
    # copied the datetime from solutions
    created_at =db.Column(db.DateTime,nullable=False,default=datetime.datetime.now)
    post_user = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)

    # referenced https://www.py4u.net/discuss/157891 for the solution down below

    # post_user = db.Column('id', db.Integer, db.ForeignKey(User.id), primary_key=True)
    



