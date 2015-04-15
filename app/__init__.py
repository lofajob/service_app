# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from tmp.mongo_orm import MongoOrm

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# initialize mongo DB
user_instant = MongoOrm(database='users')
user_instant.connect_to_db()
user_instant.switch_collection('users')

from app import views, models
