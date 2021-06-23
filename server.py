from flask import Flask, render_template, request, flash, redirect, session, url_for, Blueprint
from flask_login import login_required, current_user
from flask_paginate import Pagination, get_page_parameter
from .models import User, expenses, ExpCategory
from . import db
import csv
import sys
import logging
import json
import datetime
from sqlalchemy import text
from flask_mysqldb import MySQL
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file, show
from concurrent.futures import ThreadPoolExecutor
from . import arima, arima_train

executor = ThreadPoolExecutor(2)

server = Blueprint('server',__name__)
source = ColumnDataSource()


@server.route('/dashboard',methods=['GET','POST'])
@login_required
def dashboard():
    predicted_amount = executor.submit(arima.predict)
    pred_temp = predicted_amount.result()
    amount = str(int(pred_temp[0]))
    uid = current_user.id
    today = datetime.date.today()
    mm = today.strftime("%B")
    #Overview
    yy_mm = str(today.year) +"-"+ str(mm)
    tmonth = db.engine.execute(text("select DATE_FORMAT(expDate, '%Y-%M') as Month,  SUM(expAmount) from expenses group by DATE_FORMAT(expDate, '%Y-%M') having Month= '{}' order by Month desc".format(yy_mm)))
    tme= ""
    for row in tmonth:
        tme = row[1]
    tcat = db.engine.execute(text("select DATE_FORMAT(expDate, '%Y-%M') as Month, expCategory,catName , SUM(expAmount) from expenses left join exp_category on expCategory=exp_category.id group by DATE_FORMAT(expDate, '%Y-%M'),expCategory having Month='{}' order by Month,SUM(expAmount) desc limit 1".format(yy_mm)))
    cat=""
    for row in tcat:
        cat = row[2]
    ptoday = today.replace(month = today.month - 1)
    pmm = ptoday.strftime("%B")
    pyy_mm = str(ptoday.year) +"-"+ str(pmm)
    print(pyy_mm)
    tmonth = db.engine.execute(text("select DATE_FORMAT(expDate, '%Y-%M') as Month,  SUM(expAmount) from expenses group by DATE_FORMAT(expDate, '%Y-%M') having Month= '{}' order by Month desc".format(pyy_mm)))
    pme= ""
    for row in tmonth:
        pme = row[1]
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

    #For 5 recent transcations
    recent = expenses.query.filter_by(UserId=uid).join(ExpCategory, expenses.expCategory==ExpCategory.id).add_columns(expenses.id,expenses.expDesc, expenses.expDate, expenses.expAmount,ExpCategory.catName).order_by(expenses.expDate.desc()).limit(5)
    return render_template('dashboard.html',name = current_user.name, bar_labels = json.dumps(bar_labels), bar_data= json.dumps(bar_data),
                            pie_lables = json.dumps(pie_lables), pie_data = json.dumps(pie_data), recent=recent, this_month=tme, prev_month=pme, predictions = amount,expensivecategory=cat)


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
        curr = db.engine.execute(text("select DATE_FORMAT(expDate, '%Y-%m-%01') , SUM(expAmount) from expenses where UserId = '{}' group by DATE_FORMAT(expDate, '%Y-%m-%01')".format(userId)))
        executor.submit(arima_tocsv(curr))
        executor.submit(arima_train.train())
        return redirect(url_for('server.add_expense'))

    get_category = ExpCategory.query.filter_by()
    return render_template('add-expense.html',catlist = get_category)

@server.route('/profile', methods=['GET','POST'])
@login_required
def profile():
    uid = current_user.id
    if request.method == 'POST' :
        fname = request.form['fullname']
        mobno = request.form['contactnumber']
        db.engine.execute(text("UPDATE user SET name='{}', mobno={} where id={}".format(fname,mobno, uid)))
        flash("Profile Updated Successfully")
        return redirect(url_for('server.profile'))
    result = User.query.filter_by(id=uid)
    res = result[0]
    logging.warning(res.name)
    return render_template('user-profile.html', result=res)

@server.route('/datewise-reports',methods=['POST','GET'])
@login_required
def expensedatewisereports():
    return render_template('expense-datewise-reports.html')

@server.route('/datewise-reports-detailed',methods=['POST','GET'])
@login_required
def expensedatewisereportsdetailed():
    uid = current_user.id
    fromdate = request.form['fromdate']
    todate = request.form['todate']
    result = db.engine.execute(text("select expDate,SUM(expAmount) from expenses where expDate>='{}' and expDate<='{}' and UserId = {} group by expDate order by expDate desc".format(fromdate, todate, uid)))
    totalAmount = db.engine.execute(text("select SUM(expAmount) from expenses where expDate>='{}' and expDate<='{}' and UserId = {}".format(fromdate, todate, uid)))
    for amount in totalAmount:
        total = amount[0]
    return render_template('expense-datewise-reports-detailed.html', fdate=fromdate, tdate = todate, result=result, total=total)

@server.route('/monthwise-reports',methods=['POST','GET'])
@login_required
def expensemonthwisereports():
    return render_template('expense-monthwise-reports.html')

@server.route('/monthwise-reports-detailed',methods=['POST','GET'])
@login_required
def expensereports():
    uid = current_user.id
    fromdate = request.form['fromdate']
    todate = request.form['todate']
    fromdate = "-".join(fromdate.split('-')[0:2]) + '-' + '01'
    todate = "-".join(todate.split('-')[0:2]) + '-' + '01'
    if fromdate.split('-')[1] == todate.split('-')[1]:
        todate = todate.split('-')[0] + '-' + '0'+str(int(todate.split('-')[1]) + 1 ) + '-'+ '01'
    result = db.engine.execute(text("select DATE_FORMAT(expDate, '%Y-%m'),SUM(expAmount) from expenses where expDate>='{}' and expDate<='{}' and UserId = {} group by DATE_FORMAT(expDate, '%Y-%m')".format(fromdate, todate, uid)))
    totalAmount = db.engine.execute(text("select SUM(expAmount) from expenses where expDate>='{}' and expDate<='{}' and UserId = {}".format(fromdate, todate, uid)))
    for amount in totalAmount:
        total = amount[0]
    return render_template('monthwise-detail-reports.html', fromdate=fromdate, todate=todate, result=result, total = total)

# @server.route('/expense-reports-detailed')
# def edrd():
#     return render_template('expense-reports-detailed.html')

@server.route('/yearwise-reports')
@login_required
def expenseyearwisereports():
    return render_template('expense-yearwise-reports.html')

@server.route('/yearwise-reports-detailed',methods=['POST','GET'])
@login_required
def eywd():
    uid = current_user.id
    fromdate = request.form['fromdate']
    todate = request.form['todate']
    fromdate = "-".join(fromdate.split('-')[0:2]) + '-' + '01'
    todate = "-".join(todate.split('-')[0:2]) + '-' + '01'
    if fromdate.split('-')[0] == todate.split('-')[0]:
        todate = todate.split('-')[0] + '-' + '0'+str(int(todate.split('-')[1]) + 1 ) + '-'+ '01'
    result = db.engine.execute(text("select DATE_FORMAT(expDate, '%Y'),SUM(expAmount) from expenses where expDate>='{}' and expDate<='{}' and UserId={} group by DATE_FORMAT(expDate, '%Y')".format(fromdate, todate, uid)))
    totalAmount = db.engine.execute(text("select SUM(expAmount) from expenses where expDate>='{}' and expDate<='{}' and UserId = {}".format(fromdate, todate, uid)))
    for amount in totalAmount:
        total = amount[0]
    return render_template('expense-yearwise-reports-detailed.html', fromdate=fromdate, todate=todate, result=result, total = total)

@server.route('/manage-expense')
@login_required
def manageexpense():
    uid = current_user.id
    page = request.args.get('page', 1, type=int)
    result = expenses.query.filter_by(UserId=uid).join(ExpCategory, expenses.expCategory==ExpCategory.id).add_columns(expenses.id,expenses.expDesc, expenses.expDate, expenses.expAmount,ExpCategory.catName).order_by(expenses.expDate.desc()).paginate(page=page, per_page=20)
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

def arima_tocsv(cursor):
    c = csv.writer(open('SmtExpMngr/models/train_data.csv', 'w'))
    for x in cursor:
        c.writerow(x)
if __name__ == '__main__':
    app.run(debug=True)
