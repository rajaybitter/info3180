from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'meh'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:leelee431@localhost/web2'
db = SQLAlchemy(app)
from app import views, models