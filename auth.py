from flask import Blueprint, render_template, redirect, url_for, request

auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return render_template('index.html')

@auth.route('/signup')
def signup():
    return render_template('registration.html')


@auth.route('/signup', methods= ['POST'])
def signup():
    return render_template('registration.html')

@auth.route('/logout')
def logout():
    return redirect(url_for('login'))
