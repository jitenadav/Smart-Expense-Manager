from . import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100))
    mobno = db.Column(db.Unicode(255), nullable=False)
    regdate = db.Column(db.Date, nullable=False)


class expenses(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    expDate = db.Column(db.Date, nullable = False)
    expCategory = db.Column(db.String(50), nullable = False)
    expAmount = db.Column(db.Integer, nullable = False)
    expDesc = db.Column(db.String(100), nullable = False)
