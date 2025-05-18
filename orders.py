from audioop import reverse
from bottle import route, view, post, request
from datetime import datetime
import json
import re
from pathlib import Path

ORDERS_JSON = Path(__file__).parent / "orders.json"

def load_orders():
    if ORDERS_JSON.exists():
        with open(ORDERS_JSON, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_orders(orders):
    with open(ORDERS_JSON, 'w', encoding='utf-8') as f:
        json.dump(orders, f, ensure_ascii=False, indent=2)

@route('/orders')
@view('orders')
def show_orders():
    orders = load_orders()
    return dict(
        title='Orders',
        year=datetime.now().year,
        orders=list(reversed(orders)), # ѕередаем загруженные заказы в шаблон, 
                                       # переворачиваем дл€ того чтобы новые заказы были сверху
        show_modal=False
    )

@post('/orders')
@view('orders')
def handle_orders_post():
    name = request.forms.get('Name')
    phone = request.forms.get('Phone')
    details = request.forms.get('Details')
    orders = load_orders()
    show_modal = True                   # ¬сплывающее окно
    if check(phone):
        orders.append({'id': len(orders)+1, 'name': name, 
                       'description': details, 'phone': phone, 
                       'date': datetime.now().strftime("%Y-%m-%d"), 'link': '#'})
        save_orders(orders)
        show_modal = False

    return dict(
        title='Orders',
        year=datetime.now().year,
        orders=list(reversed(orders)),  # ѕередаем загруженные заказы в шаблон, 
                                        # переворачиваем дл€ того чтобы новые заказы были сверху
        show_modal = show_modal
    )

def check(phone):   
    return re.match(r'^8\s\(\d{3}\)\s\d{3}-\d{2}-\d{2}$', phone)