from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, SelectField, DateField
from wtforms.validators import DataRequired, Length, ValidationError
from datetime import datetime, date
from application.models import Race,Characters

#Creating a form for the Character Creation
class CreateCharacterForm(FlaskForm):
    name = StringField('Name your Character', validators=[DataRequired(), Length(min=2,max=30)])
    age = IntegerField('Input your Age',validators=[DataRequired()])
    gender = SelectField('Select Gender', choices = [('male','MALE'),('female','FEMALE')])
    class_name = SelectField('Select your Class',choices=[('bezerker','BEZERKER'),('paladin','PALADIN'),('martial artist','MARTIAL ARTIST'),('assasin','ASSASIN'),('battle mage','BATTLE MAGE')])
    date = DateField('Date of Creation',
        default=date.today,validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired(), Length(min=2,max=300)])
    character_race= SelectField('Select Race', choices=[],validators=[DataRequired()])
    submit = SubmitField('Submit Character')


class RaceForm(FlaskForm):
    name = StringField("Input your Race name", validators=[DataRequired(), Length(min=2,max=30)])
    submit = SubmitField('Submit Class Selection')

class RaceUpdateForm(FlaskForm):
    name = StringField("Input your Race name", validators=[DataRequired(), Length(min=2,max=30)])
    submit = SubmitField('Update Class Selection')
