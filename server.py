from flask import Flask, render_template, request, flash, redirect, session, url_for
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
import bcrypt
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config.from_pyfile('config.py')
# mysql = MySQL(app)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    mobno = db.Column(db.Unicode(255), nullable=False)


@app.route('/',methods=['GET','POST'])
@app.route('/login', methods =['GET', 'POST'])
def home():

#LOGIN
    msg = ""
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        details = request.form
        email = details['email']
        password = details['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO demo(email, password) VALUES (%s, %s)", (email, password))
        mysql.connection.commit()
        cur.close()
        flash("User Added")
    return render_template('index.html', msg=msg )


@app.route('/signup', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        mobno = request.form['mobilenumber']
        pswd = request.form['password']
        confpswd = request.form['repeatpassword']

        existing_email = User.query.filter_by(email=email).first()


        if(existing_email is None):
            hashpass = bcrypt.hashpw(pswd.encode('utf-8'),bcrypt.gensalt())
            new_user = User(name=name, email=email, mobno=mobno, password=hashpass)
            db.session.add(new_user)
            db.session.commit()

            flash("Successfully Signed up")
            return redirect(url_for('home'))
        elif(existing_email is not None) :
            flash('Email is Already Taken')
            return redirect(url_for('registration'))

    return render_template('registration.html')


if __name__ == '__main__':
    app.run()
