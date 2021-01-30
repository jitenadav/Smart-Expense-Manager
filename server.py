from flask import Flask, render_template, request, flash, redirect, session, url_for, Blueprint
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, current_user
from .models import User, expenses
from . import db

server = Blueprint('server',__name__)


@server.route('/dashboard',methods=['GET','POST'])
@login_required
def dashboard():
    return render_template('dashboard.html',name = current_user.name)


@server.route('/resetpassword', methods= ['POST','GET'])
def resetpassword():
    return render_template('reset_password.html')


@server.route('/add-expense',methods= ['POST','GET'])
@login_required
def add_expense():
    if request.method == 'POST':

        # userId =  # TODO: Add from Flask Login
        userId = 1
        ExpenseDate = request.form['dateexpense']
        ExpenseCategory = request.form['category']
        ExpenseAmount = request.form['amount']
        ExpenseDesc = request.form['note']

        new_expense = expenses(UserId = userId, expDate= ExpenseDate , expCategory = ExpenseCategory, expAmount = ExpenseAmount, expDesc= ExpenseDesc)
        db.session.add(new_expense)
        db.session.commit()
        flash('Transaction Added Successfully')
        return redirect(url_for('server.add_expense'))

    return render_template('add-expense.html')

# @server.route('/expense-datewise-reports',methods=['POST','GET'])
# def expensedatewisereports():
#     return render_template('expense-datewise-reports.html')
#
# @server.route('/expense-datewise-reports-detailed',methods=['POST','GET'])
# def expensedatewisereportsdetailed():
#     return render_template('expense-datewise-reports-detailed.html')
#
# @server.route('/expense-monthwise-reports',methods=['POST','GET'])
# def expensemonthwisereports():
#     return render_template('expense-monthwise-reports.html')
#
# @server.route('/expense-reports')
# def expensereports():
#     return render_template('expense-reports.html')
#
# @server.route('/expense-reports-detailed')
# def edrd():
#     return render_template('expense-reports-detailed.html')
#
# @server.route('/exepnse-yearwise-reports')
# def expenseyearwisereports():
#     return render_template('expense-yearwise-reports.html')
#
# @server.route('/expense-yearwise-reports-detailed')
# def eywd():
#     return render_template('expense-yearwise-reports-detailed.html')
#
# @server.route('/manage-expense')
# def manageexpense():
#     return render_template('manage-expense.html')


if __name__ == '__main__':
    app.run(debug=True)
