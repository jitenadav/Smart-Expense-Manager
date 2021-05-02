from flask import Flask, render_template, request, flash, redirect, session, url_for, Blueprint
from flask_login import login_required, current_user
from .models import User, expenses, ExpCategory
from . import db
import logging
import datetime
from sqlalchemy import text
from flask_mysqldb import MySQL
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file, show

server = Blueprint('server',__name__)
source = ColumnDataSource()

@server.route('/dashboard',methods=['GET','POST'])
@login_required
def dashboard():
    year = datetime.date.today().year
    result = db.engine.execute(text("select *, MONTHNAME(CONCAT(DATE,'-','01')) as datet from (select DATE_FORMAT(expDate, '%Y-%m') as DATE, SUM(expAmount) as Total_Amount from expenses group by DATE_FORMAT(expDate, '%Y-%m') having DATE={} ) as subq".format(year)))
    for row in result:
        logging.warning(row[2])
    return render_template('dashboard.html',name = current_user.name)


@server.route('/resetpassword', methods= ['POST','GET'])
def resetpassword():

    return render_template('reset_password.html')


@server.route('/add-expense',methods= ['POST','GET'])
@login_required
def add_expense():
    if request.method == 'POST':

        # userId =  # TODO: Add from Flask Login
        userId = current_user.id
        ExpenseDate = request.form['dateexpense']
        ExpenseCategory = request.form['category']
        ExpenseAmount = request.form['amount']
        ExpenseDesc = request.form['note']

        new_expense = expenses(UserId = userId, expDate= ExpenseDate , expCategory = ExpenseCategory, expAmount = ExpenseAmount, expDesc= ExpenseDesc)
        db.session.add(new_expense)
        db.session.commit()
        flash('Transaction Added Successfully')
        return redirect(url_for('server.add_expense'))

    get_category = ExpCategory.query.filter_by()
    print(type(get_category))
    return render_template('add-expense.html',catlist = get_category)

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
