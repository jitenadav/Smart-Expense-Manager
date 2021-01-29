from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    mobno = db.Column(db.Unicode(255), nullable=False)
    regdate = db.Column(db.Datetime, nullable=False)


class expenses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
