from server import db


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
<<<<<<< HEAD
    expDate = db.Column(db.Datetime, nullable = False)
    expCategory = db.Column(db.String(50), nullable = False)
    expAmount = db.Column(db.Integer, nullable = False)
    expDesc = db.Column(db.String(100), nullable = False)
=======
>>>>>>> a50dc099ec6bc49a38a6bd29b48d3780d096cc30
