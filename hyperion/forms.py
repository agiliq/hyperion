from flask_wtf import Form
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, URL, number_range


class WatcherForm(Form):

    RUN_FREQ_CHOICES = (
        ('5', '5 min'),
        ('15', '15 min'),
        ('30', '30 min'),
        ('60', '1 hour'),
        ('180', '3 hours'),
        ('360', '6 hours'),
    )

    email = StringField('Email', validators=[DataRequired(), Email()])
    url = StringField('Password', validators=[DataRequired(), URL()])
    status_code = IntegerField(
        'Status Code',
        validators=[DataRequired(), number_range(100, 599)])
    run_freq = SelectField('Run Every', choices=RUN_FREQ_CHOICES)
