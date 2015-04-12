from app import db

#ROLE_USER = 0
#ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fname = db.Column(db.String(80), unique = False)
    lname = db.Column(db.String(80), unique = False)
    login = db.Column(db.String(80), unique = True)
    email = db.Column(db.String(120), unique = True)
    role_id = db.Column(db.SmallInteger)

    def __init__(self, fname, lname, login, email, role_id):
        self.fname = fname
        self.lname = lname
        self.login = login
        self.email = email
        self.role_id = role_id

    def __repr__(self):
        return '<User %r>' % (self.login)