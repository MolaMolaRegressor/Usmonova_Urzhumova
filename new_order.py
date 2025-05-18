from bottle import post, request, view
from datetime import datetime

@post('/orders')
@view('orders')
def handle_orders_post():
    name = request.forms.get('Name')
    phone = request.forms.get('Phone')
    comment = request.forms.get('Comment')
    
    error = None
    if not name:
        error = "Product is required!"
    
    return dict(
        title="Orders",
        name=name,
        phone=phone,
        error=error,  # Передаем ошибку в шаблон
        cpmment=comment,
        date=datetime.now().date,
        year=datetime.now().year
    )
