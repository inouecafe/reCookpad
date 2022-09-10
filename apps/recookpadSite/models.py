from apps.app import db
from sqlalchemy.sql import func

class Test(db.Model):
    __tablename__ ="test"
    id = db.Column(db.Integer, primary_key="True")
    text = db.Column(db.String)