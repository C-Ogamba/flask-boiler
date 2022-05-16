from flask import render_template
from app.errors import errors

@errors.app_errorhandler(404)
def not_found(error):
    """ 404 error view function"""
    return render_template('errors/404.html')