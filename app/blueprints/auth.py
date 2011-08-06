from functools import wraps

from flask import session, redirect, request, Response
from google.appengine.api import users

from main import app

@app.route('/logout')
def logout():
    """ Clear the session """
    session.pop('user', None)
    url = request.args.get('continue')
    return redirect(users.create_logout(url))

def login_required(func):
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