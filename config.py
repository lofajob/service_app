import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Lofa666@localhost/test_db'
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = True
SECRET_KEY = 'q1234567890q'