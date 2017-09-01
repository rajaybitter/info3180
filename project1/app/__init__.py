from flask import Flask


app = Flask(__name__)


app.config['SECRET_KEY'] = "IDK"

db = SQLAlchemy(app)
app.secret_key = 'hi'
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://rajay:rajayjb$@localhost/proj1'
db = SQLAlchemy(app)

from app import views


