
import unittest
from datetime import datetime
import re
from news import handle_news_post  # Импортируем функцию для тестирования
from orders import check as check_phone  # Импортируем функцию проверки телефона
from bottle import request, response

class TestValidation(unittest.TestCase):
    
    def test_date_validation_valid(self):
        """Тест правильной даты"""
        test_cases = [
            "2023-12-31",
            "2024-01-01",
            "2000-02-29"  # Високосный год
        ]
        
        for date in test_cases:
            try:
                datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                self.fail(f"Valid date {date} failed validation")

    def test_date_validation_invalid(self):
        """Тест неправильной даты"""
        test_cases = [
            "31-12-2023",  # Неправильный формат
            "2023/12/31",  # Неправильный разделитель
            "2023-13-01",  # Несуществующий месяц
            "2023-02-30",  # Несуществующий день
            "not-a-date",  # Совсем не дата
            ""             # Пустая строка
        ]
        
        for date in test_cases:
            with self.assertRaises(ValueError):
                datetime.strptime(date, "%Y-%m-%d")

    def test_phone_validation_valid(self):
        """Тест правильного телефона"""
        valid_phones = [
            "8 (123) 456-78-90",
            "8 (999) 999-99-99",
            "8 (000) 000-00-00"
        ]
        
        for phone in valid_phones:
            self.assertTrue(check_phone(phone), f"Valid phone {phone} failed validation")

    def test_phone_validation_invalid(self):
        """Тест неправильного телефона"""
        invalid_phones = [
            "1234567890",
            "8(123)456-78-90",  # Пробелы обязательны
            "8 (123) 4567890",  # Дефисы обязательны
            "+7 (123) 456-78-90",  # Должна начинаться с 8
            "8 (123) 456-78-9",   # Не хватает цифры
            "not-a-phone",        # Совсем не телефон
            ""                    # Пустая строка
        ]
        
        for phone in invalid_phones:
            self.assertFalse(check_phone(phone), f"Invalid phone {phone} passed validation")

if __name__ == '__main__':
    unittest.main()