from app import app
from flask import render_template, url_for, redirect,flash, get_flashed_messages
from app.form import UserInputForm
from app.models import IncomeExpense
from app import db
import json



@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/add', methods=['GET', 'POST'])
def add_records():
    form = UserInputForm() 
    if form.validate_on_submit():
        expense = IncomeExpense(date=form.date.data, title=form.title.data, description=form.description.data, amount=form.amount.data, category=form.category.data, type=form.type.data)
        db.session.add(expense)
        db.session.commit()
        flash('Your expense has been added!', 'success')
        return redirect(url_for('add_records'))
    return render_template('add.html', title='Add Expense', form=form)

@app.route('/records')
def records():
    expenses = IncomeExpense.query.all()
    return render_template('records.html', title='Records', expenses=expenses)


@app.route('/delete/<int:id>')
def delete(id):
    expense = IncomeExpense.query.get_or_404(int(id))
    db.session.delete(expense)
    db.session.commit()
    flash('Your expense has been deleted!', 'success')
    return redirect(url_for('records'))

@app.route('/dashboard')
def dashboard():
    
    income_vs_expense = db.session.query(db.func.sum(IncomeExpense.amount), IncomeExpense.type).group_by(IncomeExpense.type).order_by(IncomeExpense.type).all()
    category_camparison = db.session.query(db.func.sum(IncomeExpense.amount), IncomeExpense.category).group_by(IncomeExpense.category).order_by(IncomeExpense.category).all()
    dates = db.session.query(db.func.sum(IncomeExpense.amount), IncomeExpense.date).group_by(IncomeExpense.date).order_by(IncomeExpense.date).all()
    top_categories = db.session.query(db.func.sum(IncomeExpense.amount), IncomeExpense.category).filter(IncomeExpense.type == 'expense').group_by(IncomeExpense.category).order_by(db.func.sum(IncomeExpense.amount).desc()).limit(5).all()
    total_income = db.session.query(db.func.sum(IncomeExpense.amount)).filter_by(type='income').scalar()
    total_expenses = db.session.query(db.func.sum(IncomeExpense.amount)).filter_by(type='expense').scalar()
    if total_income is None or total_expenses is None:
        savings_rate = None
    else:
        savings_rate = (total_income - total_expenses) / total_income


    income_expense = []
    for amount, type in income_vs_expense:
        income_expense.append(amount)
    
    category = []
    for amount, cat in category_camparison:
        category.append(amount)

    over_time_expenditure = []
    dates_label = []
    for amount, date in dates:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_expenditure.append(amount)

    return render_template('dashboard.html', title='Dashboard', income_vs_expense=json.dumps(income_expense), category_camparison=json.dumps(category), over_time_expenditure=json.dumps(over_time_expenditure), dates_label=json.dumps(dates_label))