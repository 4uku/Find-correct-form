import re
from pathlib import Path
from typing import List

from tinydb import TinyDB

DB_PATH = Path('db.json').resolve()
db = TinyDB(DB_PATH)

REGEX_EMAIL = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
REGEX_DATE_1 = re.compile(r'^\d{4}[-]\d{2}[-]\d{2}$')
REGEX_DATE_2 = re.compile(r'^\d{2}[.]\d{2}[.]\d{4}$')

def value_to_type(params: dict) -> dict:
    """
    Функция принимает словарь с параметрами из URL-запроса,
    затем определяет и заменяет значение каждого ключа на соответствующий тип,
    и возвращает его (словарь). Любой нераспознанный тип данных расценивается как "text"

    Запрос
    --------------
    {
        "user_name": "John Doe",
        "user_phone": "+7 123 456 78 90",
        "user_date_birth": "2001-01-01",
        "user_email": "user@mail.ru",
        "user_username": "johnnnnnny",
    }
    
    Ответ
    --------------
    {
        "user_name": "text",
        "user_phone": "phone",
        "user_date_birth": "date",
        "user_email": "email",
        "user_username": "text",
    }
    """
    for key, value in params.items():
        if value[0] == '+':
            params.update({key: 'phone'})
        elif re.fullmatch(REGEX_EMAIL, value):
            params.update({key: 'email'})
        elif re.fullmatch(REGEX_DATE_1, value) or re.fullmatch(REGEX_DATE_2, value):
            params.update({key: 'date'})
        else:
            params.update({key: 'text'})
    return params

def find_forms(params: dict) -> List[dict] | dict:
    """
    Функция принимает словарь с параметрами из URL-запроса,
    ищет соответствующий параметрам запроса шаблон в БД и возвращает
    список из словарей с именами подходящих шаблонов. Если ничего не было
    найдено, вернется словарь с входящими данными, значения которого
    изменены на соответствующий тип.

    Запрос
    --------------
    {
        "user_name": "John Doe",
        "user_phone": "+7 123 456 78 90",
        "user_date_birth": "2001-01-01",
        "user_email": "user@mail.ru",
        "user_username": "johnnnnnny",
    }

    Ответ
    --------------
    Если форма найдена:
    {
        "name": "UserForm"
    }
    Если не найдена:
    {
        "user_name": "text",
        "user_phone": "phone",
        "user_date_birth": "date",
        "user_email": "email",
        "user_username": "text",
    }
    """
    fields_and_types = value_to_type(params)
    found_forms = []
    for item in db.all():
        item = dict(item)
        name = item.pop('name')
        if item.items() <= fields_and_types.items():
            found_forms.append({'name': name})

    if found_forms:
        return found_forms
    else:
        return fields_and_types
