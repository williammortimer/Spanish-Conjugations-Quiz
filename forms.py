from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class AnswerForm(FlaskForm):
    answer = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Sign In')
