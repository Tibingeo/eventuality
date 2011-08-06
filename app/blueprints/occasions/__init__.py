# -*- coding: utf-8 -*-

from flask import Blueprint

occasions_bp = Blueprint('occasions', __name__, template_folder='templates')

import views