# app/users/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import User


class CreateUserForm(FlaskForm):
    """
    Form for creation of users
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    name = StringField('Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
                                                    DataRequired(),
                                                    EqualTo('confirm_password')
                                                    ])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Create')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already being used.')
