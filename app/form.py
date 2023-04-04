from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, FloatField, DateField
from wtforms.validators import DataRequired
from datetime import date , datetime
class UserInputForm(FlaskForm):
    
    amount = FloatField('Amount', validators=[DataRequired()])
    category = SelectField('Category', validators=[DataRequired()], choices=[('Food', 'Food'), ('Rent','Rent'),('Transportation', 'Transportation'),('Salary', 'Salary'), 
                                                                             ('Gifts', 'Gifts'),('Bonus', 'Bonus'), ('Investment', 'Investment'),
                                                                              ('Entertainment', 'Entertainment'), ('Health', 'Health'), ('Clothing', 'Clothing'), 
                                                                              ('Housing', 'Housing'), ('Utilities', 'Utilities'), ('Insurance', 'Insurance'), ('Education', 'Education'),
                                                                            ('Debt repayment', 'Debt repayment'), ('Savings', 'Savings'), ('Other', 'Other')])
    description = StringField('Description')
    date = DateField('Date', default=date.today, validators=[DataRequired()])
    
    title = StringField('Title')
    type = SelectField('Type', validators=[DataRequired()], choices=[ ('Expense', 'Expense'),('Income', 'Income')])
    submit = SubmitField('Submit')

