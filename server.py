from flask import Flask, render_template, request, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_pyfile('config.py')
mysql = MySQL(app)

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
        cursor = mysql.connection.cursor()
        existing_user = users.find_one({'uname':request.form['signupusername']})
        existing_email = users.find_one({'email':request.form['signupemail']})

        if (existing_user is None) and (existing_email is None):
            hashpass = bcrypt.hashpw(request.form['signuppassword'].encode('utf-8'),bcrypt.gensalt())
            users.insert({'uname': request.form['signupusername'],'email': request.form['signupemail'],
                            'contact': request.form['signupphone'], 'password' : hashpass,'utype':"u"})
            # session['username'] = request.form['signupusername']
            flash("Successfully Signed up")
            return redirect(url_for('home'))

        elif (existing_email is None) and (existing_user is not None):
            flash("That Username Already Exists!")
            return redirect(url_for('Signup'))

        elif (existing_user is None) and (existing_email is not None) :
            flash('Email is Already Taken')
            return redirect(url_for('Signup'))

        flash('User Already Exists')
        return redirect(url_for('Signup'))

    return render_template('registration.html')


if __name__ == '__main__':
    app.run()
