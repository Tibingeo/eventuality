# -*- coding: utf-8 -*-

from functools import wraps

from flask import session, redirect, request
from google.appengine.api import users

from auth import auth_bp as bp

__all__ = ['login_wrapper', 'logout_wrapper', 'login_required']

@bp.route('/login')
def login_wrapper():
    """ If the user is logged set the session, otherwise redirect to the GAE
    authentication system
    """
    if users.get_current_user():
        session['user'] = users.get_current_user()
        url = request.args.get('continue')
        return redirect(url)
    else:
        return redirect(users.create_login_url(request.url))

@bp.route('/logout')
def logout_wrapper():
    """ Clear the session """
    if not users.get_current_user():
        session.pop('user', None)
        url = request.args.get('continue')
        return redirect(url)
    else:
        return redirect(users.create_logout_url(request.url))

def login_required(func):
    """ Decorator for a view """
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not users.get_current_user():
            session.pop('user', None)
            return redirect(users.create_login_url(request.url))
        else:
            if not 'user' in session:
                session['user'] = users.get_current_user()
        return func(*args, **kwargs)
    return decorated_view