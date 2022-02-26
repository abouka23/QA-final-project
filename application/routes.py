from application import app, db
from application.models import Characters
from application.forms import CreateForm, UpdateForm
from flask import render_template, redirect, url_for, request

@app.route('/create', methods=['GET', 'POST'])
def create():
    createform = CreateForm()

    if createform.validate_on_submit():
        character = Characters(name=createform.name.data,age=createform.age.data,race=createform.race.data,gender=createform.gender.data,date=createform.date.data, description=createform.description.data)
        db.session.add(character)
        db.session.commit()
        # Instead of rendering a template, the next line redirects the user to the endpoint for the function called 'read'.
        return redirect(url_for('read'))
    return render_template('create.html', form=createform)

@app.route('/', methods=['GET'])
@app.route('/read', methods=['GET'])
def read():
    characters = Characters.query.all()
    return render_template('read.html', characters=characters)

@app.route('/update/<name>', methods=['GET', 'POST'])
def update(name):
    updateform = UpdateForm()
    character = Characters.query.filter_by(name=name).first()
    
    # Prepopulate the form boxes with current values when they open the page.
    if request.method == 'GET':
        updateform.name.data = character.name
        updateform.description.data = character.description
        return render_template('update.html', form=updateform)
    
    # Update the item in the databse when they submit
    else:
        if updateform.validate_on_submit():
            character.name = updateform.name.data
            character.age = updateform.age.data
            character.race = updateform.race.data
            character.gender = updateform.gender.data
            character.date = updateform.date.data
            character.description = updateform.description.data
            character.completed = updateform.completed.data
            db.session.commit()
            return redirect(url_for('read'))
    

@app.route('/delete/<name>', methods=['GET', 'POST'])
def delete(name):
        character = Characters.query.filter_by(name=name).first()
        db.session.delete(character)
        db.session.commit()
        return redirect(url_for('read'))

@app.route('/complete/<name>', methods=['GET'])
def complete(name):
    character = Characters.query.filter_by(name=name).first()
    character.completed = True
    db.session.commit()
    return redirect(url_for('read'))

@app.route('/incomplete/<name>', methods=['GET'])
def incomplete(name):
    character = Characters.query.filter_by(name=name).first()
    character.completed = False
    db.session.commit()
    return redirect(url_for('read')) 