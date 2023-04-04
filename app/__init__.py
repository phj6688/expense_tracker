from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expensesdb.db'
app.config['SECRET_KEY'] = '987654asf987rsz65x4b684k987es321sertt6854sgt654sssrt45sr4tsa'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes