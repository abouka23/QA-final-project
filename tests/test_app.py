# Import the necessary modules
from flask import url_for
from flask_testing import TestCase
from datetime import datetime, date
# import the app's classes and objects
from application import app, db
from application.forms import CreateForm, UpdateForm
from application.models import Characters
from flask import render_template

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. 
        # Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
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
        sample1 = Characters(name="AdamB",age=23,race="nord",gender="male",date=date.today(),description="creating a new character")
        # save users to database
        db.session.add(sample1)
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
        self.assertIn('creating a new character', str(response.data))
    
    def test_create(self):
        response = self.client.post(
            url_for('create'),
            data=dict(name="created name", age="23", race="orc", gender="male", date=date.today ,description="new created character"),
            follow_redirects=True
        )
        self.assertIn('created name', str(response.data))
        self.assertIn('new created character', str(response.data))

    def test_update(self):
        response = self.client.post(
            url_for('update', name='AdamB', age=23, race="nord",gender="male", date=date.today(), description="creating a new character"),
            data=dict(name="updated name", age=18, race="updated race", gender="female", date=date.today() ,description="updated character", completed=True),
            follow_redirects=True
        )
        self.assertIn('updated name', str(response.data))
        self.assertIn(18, int(response.data))
        self.assertIn('female', str(response.data))
        self.assertIn('updated character', str(response.data))
        self.assertIn('updated race', str(response.data))
        
    
    def test_delete(self):
        response =self.client.post(
            url_for('delete', name="AdamB", description="creating a new character"),
            follow_redirects=True
        )
        self.assertNotIn("AdamB", str(response.data))
        self.assertNotIn("creating a new character", str(response.data))