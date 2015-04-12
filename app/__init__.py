from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    #'mysql://restuser:q1234567890@localhost/staff'
db = SQLAlchemy(app)

from app import views, models
