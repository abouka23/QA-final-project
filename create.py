from application import db
from application.models import Characters,Race

db.drop_all()
db.create_all()