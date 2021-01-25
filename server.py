from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_pyfile('config.py')
mysql = MySQL(app)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == "POST":
        details = request.form
        email = details['email']
        password = details['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO demo(email, password) VALUES (%s, %s)", (email, password))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
