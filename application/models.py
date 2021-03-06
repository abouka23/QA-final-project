from sqlalchemy import ForeignKey
from application import db
from datetime import date

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(30), nullable=False)
    class_name = db.Column(db.String(30), nullable=False)
    date= db.Column(db.Date, nullable = False)
    description = db.Column(db.String(30),nullable=False)
    race_id = db.Column(db.Integer, db.ForeignKey('race.id')) #Foreign Key for race in the name race_id
    

class Race(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    character = db.relationship('Characters', backref='race') #Referring back to characters 