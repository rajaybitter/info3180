from flask.ext.wtf import Form
from wtforms.fields import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(Form):
    email = StringField('Email', [DataRequired(message = "This field must be filled")])
    password = PasswordField('Password', [DataRequired(message = "This field must be filled")])