from flask import FlaskForm
from forms.validators import Required, Email, EqualTo
from ..models import User
from forms import StringField, PasswordField, SubmitField, BooleanField
from forms import ValidationError


class RegistrationForm(FlaskForm):
    email = StringField('Email Address', validators=[Required(), Email()])
    username = StringField('Enter your username please', validators=[Required()])
    password = PasswordField('Password', validators=[Required(),
                                                     EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords', validators=[Required()])
    submit = SubmitField('Sign Up')
