from sqlalchemy import ForeignKey
from application import db

"""
class Classes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(30), nullable = False)
    characters = db.relationship('characters', backref='class') 
"""
class Characters(db.Model):
    character_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    #age = db.Column(db.Integer, nullable = False)
    description = db.Column(db.String(30), nullable = False)
    completed = db.Column(db.Boolean , default=False)
    #gender = db.Column(db.String(30))
    #date_of_creation = db.Column(db.Date)
    #class_id = db.Column(db.Integer, db.ForeignKey('Classes.id'), nullable = False)
