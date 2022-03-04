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
        # Here we use sqlite without a persistent database for our tests.
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
        # Create test registree
        #sample1 = Characters(name="AdamB",age=23,gender="male",date=date.today(),description="creating a new character")
        race1 = Race(name="AdamB")
        #character1 = Characters(name="name", age="23", gender="male", date=date.today(),description = "creating a new character") 
        # save users to database
        db.session.add(race1)
        #db.session.add(character1)
        db.session.commit()

    # Will be called after every test
    def tearDown(self):
        # Close the database session and remove all contents of the database
        db.session.remove()
        db.drop_all()

# Write a test class to test Read functionality
class TestCRUD(TestBase):
    
    def test_read(self):
        response = self.client.get(url_for('read'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('AdamB', str(response.data))
        
        # response = self.client.get(url_for('read'))
        # self.assertEqual(response.status_code, 200)
        # self.assertIn('AdamB', str(response.data))
        # self.assertIn('23', str(response.data))
        # self.assertIn('male', str(response.data))
        # self.assertIn('creating a new character', str(response.data))
        
    
    def test_create(self):
        response = self.client.post(
            url_for('create'),
            data=dict(name="created name"),
            follow_redirects=True
        )
        self.assertIn('created name', str(response.data))
        

    def test_update(self):
        response = self.client.post(
            url_for('updaterace', name='AdamB'),
            data=dict(name="AdamC"),
            follow_redirects=True
        )
        self.assertIn('AdamC', str(response.data))
             
    
    def test_delete(self):
        response =self.client.post(
            url_for('deleterace', name="AdamB"),
            follow_redirects=True
        )
        
        
        self.assertNotIn("AdamB", str(response.data))
        
        