#!/usr/bin/env python
#coding=utf-8

from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Email, EqualTo, DataRequired, Length, Regexp
from wtforms import ValidationError
from ..models import User


class LoginForm(Form):
    email = StringField("Email",validators=[DataRequired(),Length(3,64),Email()])
    password = PasswordField("Password",validators=[DataRequired(),Length(3,12)])
    remember_me = BooleanField("keep me logged in")
    submit = SubmitField("Sign In")

class RegistrationForm(Form):
    email = StringField("Email",validators=[DataRequired(),Length(3,64),Email()])
    username = StringField("Username",validators=[DataRequired(),Length(3,64),Regexp("^[A-Za-z][A-Za-z0-9_.]*$",0,"Usernames must have only letters, \
numbers, dots or underscores")])
    password = PasswordField("Password",validators=[DataRequired(),EqualTo("confirm_password",message="Passwords must match")])
    confirm_password = PasswordField("Confirm Password",validators=[DataRequired()])
    submit = SubmitField("Sign up")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("email already registered")

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("username already in use")

