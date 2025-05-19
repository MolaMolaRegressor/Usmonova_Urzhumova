"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime
import json
from pathlib import Path
import orders
import news

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/characters')
@view('characters')
def characters():
    """Renders the about page."""
    return dict(
        title='Characters',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/news')
@view('news')
def news_page():
    """Renders the news page."""
    return dict(
        title='News',
        year=datetime.now().year
    )