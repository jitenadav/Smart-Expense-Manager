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

if __name__ == '__main__':
    app.run()
