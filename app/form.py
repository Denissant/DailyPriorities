from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, TextAreaField


class ToDoForm(FlaskForm):
    """
    a form for submitting a task
    """
    title = StringField('Title')
    description = TextAreaField('Description')
    priority = RadioField('Priority',
                          choices=[
                (1, 'Urgent'),
                (2, 'High'),
                (3, 'Normal'),
                (4, 'Low'),
                (5, 'Optional')
            ])

    submit = SubmitField('Create')
