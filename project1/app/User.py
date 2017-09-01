from sqlalchemy import Column, Integer, String, DATETIME
from flask_sqlalchemy import SQLAlchemy
from app import db


class User(db.Model):
    """docstring for User"""
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    firstname = Column(String(100))
    lastname = Column(String(100))
    age = Column(String(3))
    sex = Column(String(5))
    image = Column(String(200))
    date_added = Column(String)
    username = Column(String)

    def __init__(self, firstname, lastname, age, sex, image, date_added, username, biography):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.sex = sex
        self.image = image
        self.date_added = date_added
        self.username = username
        self.biography = biography