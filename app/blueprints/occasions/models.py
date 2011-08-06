# -*- coding: utf-8 -*-

from google.appengine.ext import db
from flaskext import wtf
from flaskext.wtf import validators

class Occasion(db.Model):
    """
    A container of events.
    """
    title = db.StringProperty(required = True)
    description = db.TextProperty(required = True)
    date_start = db.DateProperty(required = True)
    date_end = db.DateProperty(required = True)
    author = db.UserProperty(required = True)


class OccasionForm(wtf.Form):
    title = wtf.TextField('Title', validators=[validators.Required()])
    description = wtf.TextAreaField('Description', validators=[validators.Required()])
    date_start = wtf.DateField('Date Start', format='%d/%m/%Y', validators=[validators.Required()])
    date_end = wtf.DateField('Date End', format='%d/%m/%Y', validators=[validators.Required()])
    delete = wtf.BooleanField('Delete')