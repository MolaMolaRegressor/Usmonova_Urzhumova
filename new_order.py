from bottle import post, request, view
from datetime import datetime

@post('/orders')
@view('orders')
def handle_orders_post():
    product = request.forms.get('Product')
    email = request.forms.get('Email')
    
    error = None
    if not product:
        error = "Product is required!"
    
    return dict(
        title="Order",
        product=product,
        email=email,
        error=error,  # Передаем ошибку в шаблон
        year=datetime.now().year
    )
