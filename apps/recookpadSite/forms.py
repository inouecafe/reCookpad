from flask_wtf import FlaskForm
from wtforms import StringField

class TestForm(FlaskForm):
    test = StringField()