from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
class CreatePostForm(FlaskForm):
    author = StringField('Author', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
            
class DeleteForm(FlaskForm):
    submit = SubmitField('Delete')

class EditForm(FlaskForm):
    author = StringField('Author', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField('Save')
