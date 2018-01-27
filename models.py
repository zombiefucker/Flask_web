#encoding:utf-8

from exts import db
from datetime import datetime

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(20),nullable=False)
    password = db.Column(db.String(100),nullable=False)

class Articles(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200),nullable=False)
    content = db.Column(db.Text,nullable=False)
    time = db.Column(db.DateTime,default=datetime.now)

    author_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    author = db.relationship('Users',backref=db.backref('articles'))