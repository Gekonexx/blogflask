from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


def validate_username(username):
    user = User.query.filer_by(username.data).first()
    if user:
        raise ValidationError('Username is already taken, please choose different one.')


def validate_email(email):
    email = User.query.filer_by(email.data).first()
    if email:
        raise ValidationError('Username email is taken, please choose different one.')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=16)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password',
                                                                                             message="The password must be equal to the one above")])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=16)])
    remember = BooleanField("Remember me")
    submit = SubmitField('Login')
