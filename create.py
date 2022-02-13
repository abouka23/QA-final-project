from application import db
from application.models import Characters

db.drop_all()
db.create_all()