from flask import Blueprint, render_template, redirect, url_for, request, flash
import bcrypt
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date
from .models import User
from . import db

auth = Blueprint('auth',__name__)

@auth.route('/login')
@auth.route('/')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('server.dashboard'))
    return render_template('index.html')


@auth.route('/login', methods = ['POST'])
def login_post():
    email = request.form['email']
    pswd = request.form['password']
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(email=email).first()
    if user:
        if check_password_hash(user.password, pswd):
            login_user(user, remember=remember)
            return redirect(url_for('server.dashboard'))
    flash("Please check your login credentials")
    return redirect(url_for('auth.login'))


@auth.route('/signup')
def signup():
    return render_template('registration.html')


@auth.route('/signup', methods= ['POST'])
def signup_post():
    name = request.form['name']
    email = request.form['email']
    mobno = request.form['mobilenumber']
    pswd = request.form['password']
    confpswd = request.form['repeatpassword']

    existing_email = User.query.filter_by(email=email).first()


    if(existing_email is None):
        hashpass = generate_password_hash(pswd, method='sha256')
        new_user = User(name=name, email=email, mobno=mobno, password=hashpass, regdate = date.today())
        db.session.add(new_user)
        db.session.commit()

        flash("Successfully Signed up")
        return redirect(url_for('auth.login'))
    elif(existing_email is not None) :
        flash('Email is Already Taken')
        return redirect(url_for('auth.signup'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
