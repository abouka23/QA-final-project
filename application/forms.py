from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, SelectField, DateField
from wtforms.validators import DataRequired, Length, ValidationError

class CreateForm(FlaskForm):
    name = StringField('Name your Character', validators=[DataRequired(), Length(min=2,max=30)])
    age = IntegerField('Input your Age',validators=[DataRequired()])
    gender = SelectField('Select Gender', choices = [('male','MALE'),('female','FEMALE')])
    date = DateField('Date of Creation',validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired(), Length(min=2,max=300)])
    submit = SubmitField('Submit Character')

class UpdateForm(FlaskForm):
    name = StringField('Title', validators=[DataRequired(), Length(min=2,max=30)])
    age = IntegerField('Input your Age',validators=[DataRequired()])
    gender = SelectField('Select Gender', choices = [('male','MALE'),('female','FEMALE')])
    date = DateField('Date of Creation',validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired(), Length(min=2,max=300)])
    completed = BooleanField('Completed')
    submit = SubmitField('Update Character')

