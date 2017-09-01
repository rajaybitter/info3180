from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from app import db


class User(db.Model):
    """Model for a User profile"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(6))

    def __init__(self, name=None, email=None, password=None, age=None, gender=None):
        self.name = name
        self.email = email
        self.password = password
        self.age = age
        self.gender = gender

    def __repr__(self):
        return '<User %r>' % self.name

    def validate(self):
        user = User.query.filter_by(email=self.email).first()
        if user == None:
            return False
        if user.password == self.password:
            return True
        else:
            return False

    def serialize(self):
        return{
            "id": self.id,
            "name" : self.name,
            "email": self.email,
            "password": self.password,
            "age": self.age,
            "gender": self.gender
        }

    def is_authenticated(self):
        return True

    def is_active(self):
        return False

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id) 