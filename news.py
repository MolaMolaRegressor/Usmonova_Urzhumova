from bottle import route, view, post, request 
from datetime import datetime  
import json  # Импортируем json для работы с JSON файлами
import re  # Импортируем re для работы с регулярными выражениями
from pathlib import Path  # Импортируем Path для работы с файловыми путями


NEWS_JSON = Path(__file__).parent / "data" / "news.json"

# Функция для загрузки новостей из JSON файла
def load_news():
    try:
        # Проверяем, существует ли файл
        if NEWS_JSON.exists():
            with open(NEWS_JSON, 'r', encoding='utf-8') as f:  # Открываем файл для чтения
                return json.load(f)  # Загружаем и возвращаем данные
        return []  # Если файл не найден, возвращаем пустой список
    except:
        return []  

# Функция для сохранения новостей в JSON файл
def save_news(news):
    with open(NEWS_JSON, 'w', encoding='utf-8') as f:  
        json.dump(news, f, ensure_ascii=False, indent=2)  # Сохраняем новости в формате JSON

@route('/news')  # Определяем маршрут для получения новостей
@view('news')  # Указываем шаблон для отображения новостей
def show_news():
    news = load_news()  # Загружаем новости
    return dict(
        title='Latest Releases',  # Заголовок страницы
        year=datetime.now().year,  # Текущий год
        news=list(reversed(news)),  # Переворачиваем список новостей, чтобы самые свежие были первыми
        show_modal=False  # Переменная для управления отображением модального окна
    )

@post('/news')  # Определяем маршрут для обработки POST-запроса на добавление новостей
@view('news')  # Указываем шаблон для отображения новостей
def handle_news_post():
    author = request.forms.get('Author')  # Получаем автора новости из формы
    description = request.forms.get('Description')  # Получаем описание новости из формы
    date = request.forms.get('Date')  # Получаем дату из формы
    news = load_news()  # Загружаем существующие новости
    show_modal = False  # Изначально устанавливаем значение для показа модального окна
    
    # Проверка корректности даты
    try:
        datetime.strptime(date, "%Y-%m-%d")  
        # Если дата корректна, добавляем новую новость
        news.append({
            'id': len(news)+1,  # Устанавливаем уникальный идентификатор
            'author': author,  # Сохраняем автора
            'description': description,  # Сохраняем описание
            'date': date,  # Сохраняем дату
            'added_date': datetime.now().strftime("%Y-%m-%d %H:%M")  # Сохраняем дату добавления
        })
        save_news(news)  # Сохраняем обновленный список новостей
    except ValueError:
        show_modal = True  # Если дата некорректна, устанавливаем флаг для показа модального окна

    return dict(
        title='Latest Releases',
        year=datetime.now().year,
        news=list(reversed(news)),  # Возвращаем новости в перевернутом порядке
        show_modal=show_modal  # Отправляем флаг для показа модального окна
    )