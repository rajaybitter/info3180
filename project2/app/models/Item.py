from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from app import db


class Item(db.Model):
    """Model for a User profile"""
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(80))
    url = db.Column(db.String(255))
    owner = db.Column(db.Integer)
    thumbnail_url = db.Column(db.String(255))

    def __init__(self, title=None, description=None, url=None, owner=None, thumbnail_url=None):
        self.title = title
        self.description = description
        self.url = url
        self.owner = owner
        self.thumbnail_url = thumbnail_url

    def __repr__(self):
        return '<Item %r>' % self.title

    def serialize(self):
        return{
            "id": self.id,
            "title" : self.title,
            "description": self.description,
            "url": self.url,
            "thumbnail_url": self.thumbnail_url
        }