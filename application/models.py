from application import db
from datetime import datetime


class Tasks(db.Model):
    id = db.Column(db.interger, primary_key=True)
    description = db.Column(db.string(100), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    date_created =db.Column(db.DateTime, default=datetime.now())