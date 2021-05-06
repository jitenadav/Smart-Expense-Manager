from flask import Blueprint, render_template, redirect, url_for, request, flash
import bcrypt
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date
from sqlalchemy import text
import logging
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

@auth.route('/resetpassword', methods=['POST','GET'])
def resetpassword():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['newpassword']
        cpassword = request.form['confirmpassword']
        existing_email = User.query.filter_by(email=email).first()

        if existing_email is None:
            flash("User doesn't Exists")
            return redirect(url_for('auth.resetpassword'))
        else:
            hashpass = generate_password_hash(password, method='sha256')
            db.engine.execute(text("UPDATE user SET password='{}' where email='{}'".format(hashpass,email)))
            flash("Password Updated")
            return redirect(url_for('auth.resetpassword'))
    return render_template('reset_password.html')

@auth.route('/changepassword', methods=['POST','GET'])
@login_required
def changepassword():
    uid = current_user.id
    if request.method == 'POST':
        ppassword = request.form['currentpassword']
        npassword = request.form['newpassword']
        cpassword = request.form['confirmpassword']

        hashpass = generate_password_hash(npassword, method='sha256')

        db.engine.execute(text("UPDATE user SET password='{}' where id='{}'".format(hashpass,uid)))
        flash("Password Changed")
        return redirect(url_for('auth.changepassword'))
    return render_template('change-password.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
