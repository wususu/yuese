from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from db.db_config import DB_URL
from lib.tools import md5

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
db = SQLAlchemy(app, use_native_unicode="utf8")


class AuthorUser(db.Model):
    __tablename__ = 'author_user'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(20), nullable=False)
    create_time = db.Column(db.DateTime, default=str(datetime.now())[:-7])
    status = db.Column(db.Integer, default=0)
    type = db.Column(db.Integer, nullable=False)
    unique = db.Column(db.String(200), nullable=False, unique=True)
    author_name = db.Column(db.String(55), nullable=True)

    def __init__(self, author_id, username, type):
        self.author_id = author_id
        self.username = username
        self.type = type
        self.unique = md5(str(author_id + username))

    def __repr__(self):
        return '<Post %r %r>' % (self.username, self.author_id)

if __name__ == '__main__':
    db.create_all()
