from sqlalchemy import ForeignKey
from application import db
from datetime import date

class Characters(db.Model):
    character_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    race = db.Column(db.String(30), nullable=False)
    gender = db.Column(db.String(30), nullable=False)
    date= db.Column(db.Date, nullable = False)
    description = db.Column(db.String(30),nullable=False)
    completed = db.Column(db.Boolean , default=False)
    
