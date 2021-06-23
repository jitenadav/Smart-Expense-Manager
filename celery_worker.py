from flask import Flask
from celery import Celery
import uwsgi

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top-secret@sfhg!'
# Celery configuration
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task
def predictExpense(self):
    return render_template("<html><body> <h1> Here we will be predictiing the next month expenses usign ARIMA model </h1></body></html>")

@app.route('/getpred')
def getpred():
    code = predictExpense()
