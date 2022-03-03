from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:uC!qUv3QqpEi5Lap@localhost:3306/racedb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'hreuifh7ueyhf'

db = SQLAlchemy(app)

from application import routes