from flask.ext.wtf import Form
from wtforms.fields import StringField, PasswordField, DecimalField, FileField
from wtforms import RadioField
from wtforms.validators import DataRequired


class RegisterForm(Form):
	name = StringField('Name', [DataRequired(message = "This field must be filled")])
	email = StringField('Email', [DataRequired(message = "This field must be filled")])
	gender = RadioField('Gender', [DataRequired(message = "This field must be filled")], choices=[('male', 'Male'), ('female', 'Female')])
	password = PasswordField('Password', [DataRequired(message = "This field must be filled")])
	age = DecimalField('Age', [DataRequired(message = "This field must be filled")])