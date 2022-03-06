from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import getenv 


app = Flask(__name__)

#Using os.getenv to hide MySQL database details
#export DATABASE_URI='mysql+pymysql://<user>:<password>@<host_ip>/testdb' has to be called on every session start.
#Otherwise application and pytest won't function
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'efefwgwrgwr'

db = SQLAlchemy(app)

from application import routes