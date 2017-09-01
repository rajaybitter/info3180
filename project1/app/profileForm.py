from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, DecimalField, TextAreaField, FileField, SelectField, validators


class profileForm(Form):
    firstname = StringField(
        'firstname', [validators.Required(message="This field cannot be empty"), validators.Length(min=2, max=25)])
    lastname = StringField(
        'lastname', [validators.Required(message="This field cannot be empty"), validators.Length(min=2, max=25)])
    username = StringField('username', [validators.Required(message = "This field cannot be empty"), validators.Length(min=4, max=25)])
    age = DecimalField(
        'age', [validators.Required(message="This field cannot be empty")])
    image = FileField('image')
    sex = SelectField('sex', choices=[('male', 'Male'), ('female', 'Female')])
    biography = TextAreaField('biography', [validators.Required(message="This field cannot be empty"), validators.Length(min=8, max=50)])