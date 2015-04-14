# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import TextField, StringField,BooleanField, validators
from wtforms.validators import Required


class AddUser(Form):
    fname = TextField('First Name', [validators.Required()])
    lname = TextField('Last Name', [validators.Required()])
    login = TextField('Login', [validators.Required()])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])


class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remeber_me', default = False)