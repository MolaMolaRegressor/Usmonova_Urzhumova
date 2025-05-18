"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime
import json
from pathlib import Path
import orders

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



#@route('/orders')
#@view('orders')
#def orders():
#    # Здесь может быть загрузка существующих заказов из БД
#    sample_orders = [
#        {
#            'id': '1',
#            'product': 'Book',
#            'description': 'First test order description',
#            'phone': '+7 (904) 912 71 40',
#            'date': '08-12-2025',
#            'link': '#'
#        },
#        {
#            'id': '2',
#            'product': 'Manhua',
#            'description': 'Second test order description', 
#            'phone': '+7 (904) 912 71 40',
#            'date': '08-12-2025',
#            'link': '#'
#        }
#    ]
#    return dict(
#        title='Orders',
#        year=datetime.now().year,
#        orders=sample_orders  # Передаем список заказов
#    )

##@route('/orders')
##@view('orders')
##def orders():
##    """Renders the about page."""
##    return dict(
##        title='Orders',
##        message='Your application description page.',
##        year=datetime.now().year
##    )
