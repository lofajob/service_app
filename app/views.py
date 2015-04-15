# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect, url_for, request

from app import app, db, user_instant
from forms import LoginForm, AddUser
from models import User, Role


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Main Page')


@app.route('/userslist')
def userslist():
    context = User.query.all()

    return render_template('users_list.html', context=context)\


@app.route('/mongo/users_list')
def mongo_userslist():
    context = user_instant.select_all()

    return render_template('users_list.html', context=context)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    roles = Role.query.all()
    form = AddUser()

    if request.method == 'POST' and form.validate_on_submit():
        if request.form['user_role'] != '':
            role = Role.query.filter_by(\
                                        id=request.form['user_role']).first()
            user = User(form.fname.data, form.lname.data, form.login.data,\
                        form.email.data, role)
            db.session.add(user)
            db.session.commit()
            flash('%s %s was successfully added to Data Base'\
                   % (form.lname.data,form.fname.data))
            return redirect(url_for('userslist'))

    return render_template('add_user.html', roles=roles, form=form)


@app.route('/mongo_add', methods=['GET', 'POST'])
def mongo_add():
    form = AddUser()
    if request.method == 'POST' and form.validate_on_submit():
        if request.form['user_role'] != '':
            # parsing role values
            role = {}

            role_unicod = request.form['user_role']

            id = role_unicod[3:4]
            id = int(id)

            name_start = role_unicod.find('role_name')
            name_end = len(role_unicod)
            name = role_unicod[name_start+10:name_end]

            role['id'] = id
            role['role_name'] = name

            # insert data to DB
            user_instant.insert(fname=form.fname.data, lname=form.lname.data,\
                                login=form.login.data, email=form.email.data,\
                                role=role)
            return redirect(url_for('mongo_userslist'))

    return render_template('mongo_add.html', form=form)


@app.route('/test', methods=['GET', 'POST'])
def test():
    """fuction for debugging"""
    roles = Role.query.all()
    r = request.path

    if request.method == 'POST':
        if request.form['user_role'] != '':
            role = {}

            role_unicod = request.form['user_role']

            id = role_unicod[3:4]
            id = int(id)

            name_start = role_unicod.find('role_name')
            name_end = len(role_unicod)
            name = role_unicod[name_start+10:name_end]

            role['id'] = id
            role['name'] = name
        #return redirect('/userslist')
            #vacansy = Role.query.filter_by(\
            #                            id=request.form['user_role']).first()
            return render_template('test.html', roles=roles, message = name)

    return render_template('test.html', roles=roles, message=r)


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