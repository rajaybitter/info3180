from flask.ext.wtf import Form
from wtforms.fields import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired


class ContactForm(Form):
    Name = StringField('Name')
    Email = StringField('Email')
    Subject = StringField('Subject')
    Message = TextAreaField('Message')
