# -*- coding: utf-8 -*-

#Include the libraries in the path.
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'distlib'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'blueprints'))

from flask import Flask
from occasions import occasions_bp
from auth import auth_bp

app = Flask(__name__)
app.config.from_object('settings')

app.register_blueprint(occasions_bp)
app.register_blueprint(auth_bp)

import views

from google.appengine.ext.webapp.util import run_wsgi_app

def main():
    """ Run "cached" WSGI application. """
    app.logger.debug(app.url_map)
    run_wsgi_app(app)

if __name__ == '__main__':
    main() # run main on first import