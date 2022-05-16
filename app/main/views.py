from flask import render_template
from app.main import main

@main.route('/')
@main.route('/index')
def index():
    """view function that displays homepage"""

    title = 'Home'
    return render_template('index.html', title=title)