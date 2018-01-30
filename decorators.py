# encoding:utf-8

from functools import wraps
from flask import session,redirect,url_for

# The login limit
def login_limit(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('user_id'):
            return func(*args,**kwargs)
        else:
            return redirect(url_for('Login'))
    return wrapper