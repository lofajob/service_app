# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect, url_for, request

from app import app, db
from forms import LoginForm, AddUser
from models import User, Role


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Main Page')


@app.route('/userslist')
def userslist():
    context = User.query.all()

    return render_template('users_list.html', context=context)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    roles = Role.query.all()
    form = AddUser()

    if form.validate_on_submit():
        user = User(form.fname, form.lname, form.login, form.email, )
        db.session.add(user)
        db.session.commit()
        return redirect('/userslist')
    return render_template('add.html', roles=roles, form=form)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data +\
               '"remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
                            title = 'Sign in',
                            form = form)