# -*- coding: utf-8 -*-

from flask import render_template

from main import app
#@app.route('/')
def homepage():
    """ The home page of eventuality """
    return render_template('homepage.html')
