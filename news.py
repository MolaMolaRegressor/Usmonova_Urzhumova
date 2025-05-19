from bottle import route, view, post, request
from datetime import datetime
import json
import re
from pathlib import Path

NEWS_JSON = Path(__file__).parent / "data" / "news.json"

def load_news():
    try:
        if NEWS_JSON.exists():
            with open(NEWS_JSON, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
    except:
        return []

def save_news(news):
    with open(NEWS_JSON, 'w', encoding='utf-8') as f:
        json.dump(news, f, ensure_ascii=False, indent=2)

@route('/news')
@view('news')
def show_news():
    news = load_news()
    return dict(
        title='Актуальные новинки',
        year=datetime.now().year,
        news=list(reversed(news)),
        show_modal=False
    )

@post('/news')
@view('news')
def handle_news_post():
    author = request.forms.get('Author')
    description = request.forms.get('Description')
    date = request.forms.get('Date')
    news = load_news()
    show_modal = True
    
    # Проверка даты
    try:
        datetime.strptime(date, "%Y-%m-%d")
        show_modal = False
        news.append({
            'id': len(news)+1, 
            'author': author, 
            'description': description, 
            'date': date,
            'added_date': datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        save_news(news)
    except ValueError:
        pass

    return dict(
        title='Актуальные новинки',
        year=datetime.now().year,
        news=list(reversed(news)),
        show_modal=show_modal
    )
