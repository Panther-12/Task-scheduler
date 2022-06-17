from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired, InputRequired


class TodoForm(FlaskForm):
	text = StringField('Enter task to perform:',validators=[DataRequired()])
	submit = SubmitField('Create')