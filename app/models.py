from app import db
from datetime import datetime

class IncomeExpense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, unique=False, default=datetime.today().strftime('%d-%m-%y'))
    title = db.Column(db.String(100), nullable=True)
    description = db.Column(db.String(100), nullable=True)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(20), nullable=False)
    type = db.Column(db.String(10), nullable=False)

    def __str__(self):
        return f"Expense('{self.date}', '{self.description}', '{self.amount}')"