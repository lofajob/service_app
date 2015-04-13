# -*- coding: utf-8 -*-

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fname = db.Column(db.String(80), unique = False)
    lname = db.Column(db.String(80), unique = False)
    login = db.Column(db.String(80), unique = True)
    email = db.Column(db.String(120), unique = True)

    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    role = db.relationship('Role', backref=db.backref('users', lazy='dynamic'))

    def __init__(self, fname, lname, login, email, role):
        self.fname = fname
        self.lname = lname
        self.login = login
        self.email = email
        self.role = role

    def __repr__(self):
        return '<User %r>' % (self.login)


class Role(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    role_name = db.Column(db.String(80), unique = True)

    def __init__(self, role_name):
        self.role_name = role_name

    def __repr__(self):
        return '%s' % (self.role_name)