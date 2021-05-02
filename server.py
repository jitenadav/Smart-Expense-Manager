from flask import Flask, render_template, request, flash, redirect, session, url_for, Blueprint
from flask_login import login_required, current_user
from flask_paginate import Pagination, get_page_parameter
from .models import User, expenses, ExpCategory
from . import db
import logging
import json
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
    uid = current_user.id
    # Bar graph Year's Expense
    year = datetime.date.today().year
    months = {'January':0,'February':0,'March':0,'April':0,'May':0,'June':0,'July':0,'August':0,'September':0,'October':0,'November':0,'December':0}
    result = db.engine.execute(text("select *, MONTHNAME(CONCAT(DATE,'-','01')) as datet from (select DATE_FORMAT(expDate, '%Y-%m') as DATE, SUM(expAmount) as Total_Amount from expenses where UserId ={} group by DATE_FORMAT(expDate, '%Y-%m') having DATE={} ) as subq".format(uid,year)))
    for row in result:
        months[row[2]] = int(row[1])
    bar_labels = list(months.keys())
    bar_data = list(months.values())

    # Pie chart Month's Expense
    month = '0'
    month += str(datetime.date.today().month)
    piresult = db.engine.execute(text("select catName,DATE_FORMAT(expDate,'%Y-%m') as Month, SUM(expAmount) from expenses e, exp_category c where e.expCategory = c.id and UserId={} group by expCategory,DATE_FORMAT(expDate,'%Y-%m') having Month = '{}-{}';".format(uid,year,month)))
    pie_lables = []
    pie_data = []
    for row in piresult:
        pie_lables.append(row[0])
        pie_data.append(int(row[2]))
    return render_template('dashboard.html',name = current_user.name, bar_labels = json.dumps(bar_labels), bar_data= json.dumps(bar_data),
                            pie_lables = json.dumps(pie_lables), pie_data = json.dumps(pie_data))


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

@server.route('/profile')
@login_required
def profile():
    return render_template('user-profile.html')

@server.route('/datewise-reports',methods=['POST','GET'])
def expensedatewisereports():
    return render_template('expense-datewise-reports.html')

@server.route('/datewise-reports-detailed',methods=['POST','GET'])
def expensedatewisereportsdetailed():
    return render_template('expense-datewise-reports-detailed.html')
#
@server.route('/monthwise-reports',methods=['POST','GET'])
def expensemonthwisereports():
    return render_template('expense-monthwise-reports.html')
#
# @server.route('/expense-reports')
# def expensereports():
#     return render_template('expense-reports.html')
#
# @server.route('/expense-reports-detailed')
# def edrd():
#     return render_template('expense-reports-detailed.html')
#
@server.route('/yearwise-reports')
def expenseyearwisereports():
    return render_template('expense-yearwise-reports.html')
#
@server.route('/yearwise-reports-detailed')
def eywd():
    return render_template('expense-yearwise-reports-detailed.html')
#
@server.route('/manage-expense')
@login_required
def manageexpense():
    uid = current_user.id
    page = request.args.get('page', 1, type=int)
    result = expenses.query.filter_by(UserId=uid).order_by(expenses.expDate.desc()).paginate(page=page, per_page=20)
    return render_template('manage-expense.html', result=result)

@server.route('/manage/delete/<id>')
@login_required
def delete_record(id=None):
    if id==None:
        redirect(url_for(dashboard))
    result = db.engine.execute(text("delete from expenses where id={}".format(id)))
    if result:
        flash("Record Deleted")
        return redirect(url_for('server.manageexpense'))

if __name__ == '__main__':
    app.run(debug=True)
