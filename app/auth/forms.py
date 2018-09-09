from flask import FlaskForm
from wtforms.validators import Required, Email, EqualTo
from ..models import User
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import ValidationError
