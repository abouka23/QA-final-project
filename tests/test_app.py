from flask import url_for
from flask_testing import TestCase
from datetime import datetime, date
# import the app's classes and objects
from application import app, db
from application.forms import CreateCharacterForm, RaceForm, RaceUpdateForm
from application.models import Characters, Race
from flask import render_template

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. 
        # We use our own database to produce testing
        app.config.update(SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:uC!qUv3QqpEi5Lap@localhost:3306/racedb",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    # Will be called before every test
    def setUp(self):
        # Create table
        db.create_all()
        # Create test registers for both databases
        #sample1 = Characters(name="AdamB",age=23,gender="male",date=date.today(),description="creating a new character")
        race1 = Race(name="race1")
        character1 = Characters(name="AdamB", age="23", gender="male",class_name = "bezerker", date=date.today(),description = "creating a new character") 
        # save users to databases
        db.session.add(race1)
        db.session.add(character1)
        db.session.commit()

    # Will be called after every test
    def tearDown(self):
        # Close the database session and remove all contents of the database
        db.session.remove()
        db.drop_all()

# Write a test class to test Read functionality for both the race and the characters
class TestCRUD(TestBase):
    
    def test_read(self):
        response = self.client.get(url_for('read'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('race1', str(response.data))
        
    def test_read_characters (self):
        response = self.client.get(url_for('read'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('AdamB', str(response.data))
        self.assertIn('23', str(response.data))
        self.assertIn('male', str(response.data))
        self.assertIn('bezerker',str(response.data))
        self.assertIn('creating a new character', str(response.data))   
    #testing the create functionality for both the characters and race
    def test_create(self):
        response = self.client.post(
            url_for('create'),
            data=dict(name="created name"),
            follow_redirects=True
        )
        self.assertIn('created name', str(response.data))
   
    def test_create_character(self):
        response = self.client.post(
            url_for('create_character'),
            data=dict(name="AdamB", age="23", gender="male",class_name = "bezerker", date=date.today(),description = "creating a new character"),
            follow_redirects=True
        )
        self.assertIn('AdamB', str(response.data))
        self.assertIn("23", str(response.data))
        self.assertIn("male", str(response.data))
        self.assertIn("bezerker", str(response.data))
        self.assertIn("creating a new character", str(response.data))    
#testing the update functionality.
# name is originally race1, so the data in the dictionaity will update to race 2. Then you should assert
    def test_update(self):
        response = self.client.post(
            url_for('updaterace', name='race1'),
            data=dict(name="race2"),
            follow_redirects=True
        )
        self.assertIn('race2', str(response.data))
             
    #Testing the Delete functionality for both race and characters
    def test_delete(self):
        response =self.client.get(
            url_for('deleterace', name="race1"),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertNotIn("race1", str(response.data))
        
    def test_delete_character(self):
        response =self.client.get(
            url_for('deletecharacter', name="AdamB", age="23", gender="male",class_name = "bezerker", date=date.today(),description = "creating a new character"),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertNotIn("AdamB", str(response.data))
        self.assertNotIn("23", str(response.data))
        self.assertNotIn("male", str(response.data))
        self.assertNotIn("bezerker", str(response.data))
        self.assertNotIn("creating a new character", str(response.data))