from application import app, db
from application.models import Characters,Race
from application.forms import CreateCharacterForm, RaceForm, UpdateForm
from flask import render_template, redirect, url_for, request

@app.route('/create-class', methods=['GET', 'POST'])
def create():
    createform = RaceForm()

    if createform.validate_on_submit():
        races = Race(name=createform.name.data)
        db.session.add(races)
        db.session.commit()
        return redirect(url_for('read'))
    return render_template('create_class.html', form=createform)

@app.route('/create-character', methods=['GET', 'POST'])
def create_character():
    createform = CreateCharacterForm()
    races = Race.query.all()
    for race in races:
        createform.character_race.choices.append((race.id,f"{race.name}"))
        

    if createform.validate_on_submit():
        characters = Characters(name=createform.name.data,age=createform.age.data,gender=createform.gender.data,date=createform.date.data,
        description=createform.description.data,race_id=createform.character_race.data)
        #races = Races.query.all() 
        db.session.add(characters)
        db.session.commit()
        return redirect(url_for('read'))
    return render_template('create.html', form=createform)   

    



@app.route('/', methods=['GET'])
@app.route('/read', methods=['GET'])
def read():
    #characters = Characters.query.all()
    race = Race.query.all()
    return render_template('read.html',  race=race)

@app.route('/update/<name>', methods=['GET', 'POST'])
def update(name):
    updateform = UpdateForm()
    character = Characters.query.filter_by(name=name).first()
    
    # Prepopulate the form boxes with values already submitted.
    if request.method == 'GET':
        updateform.name.data = character.name
        updateform.age.data = character.age
        updateform.gender.data = character.gender
        updateform.date.data = character.date
        updateform.description.data = character.description
        return render_template('update.html', form=updateform)
    
    # Update any fields if user needs to, returns to read page after changes made.
    else:
        if updateform.validate_on_submit():
            character.name = updateform.name.data
            character.age = updateform.age.data
            character.gender = updateform.gender.data
            character.date = updateform.date.data
            character.description = updateform.description.data
            db.session.commit()
            return redirect(url_for('read'))
    

@app.route('/delete/<name>', methods=['GET', 'POST']) # "GET request "
def delete(name):
        character = Characters.query.filter_by(name=name).first()
        db.session.delete(character)
        db.session.commit()
        return redirect(url_for('read')) # returns to read page once character is deleted.
