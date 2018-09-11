from flask import FlaskForm
from forms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from forms.validators import Required, Email, EqualTo
from ..models import User
from wtforms import ValidationError


class UpdateProfile(FlaskForm):
    bio = TextAreaField('YOU AS A USER', validators=[Required()])
    submit = SubmitField('SUBMIT')
