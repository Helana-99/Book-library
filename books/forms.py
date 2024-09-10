from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired, Length


class BookForm(FlaskForm):
    title = StringField('title', validators=[DataRequired(), Length(min=4, max=40)])
    description = StringField('description')
    image = StringField('image')
    num_pages = IntegerField('Number of pages')
    submit = SubmitField('Add')
