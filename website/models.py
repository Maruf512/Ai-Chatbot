from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Conversion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ai = db.Column(db.String(10000))
    parson = db.Column(db.String(10000))
    user = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    user_data = db.relationship('Conversion')

