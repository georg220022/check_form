import re
import json

from fastapi import HTTPException, Request
from datetime import datetime as dt


REGEX = re.compile(
    r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
)  # Честно скопированная регулярка со стаковерфлоу ))


def date_validator(obj: str) -> str | bool:
    """Проверяем на 2 доступных в ТЗ формата: 'DD.MM.YYYY' или 'YYYY-MM-DD'"""
    try:
        dt.strptime(obj, "%d.%m.%Y")
    except ValueError:
        try:
            dt.strptime(obj, "%Y-%m-%d")
        except ValueError:
            return False
    return obj


def phone_validator(phone: str) -> str | bool:
    """Валидация только для РУ номера формата '+7 xxx xxx xx xx' по ТЗ"""
    phone = phone.replace(" ", "")  # Убираем пробелы
    try:
        int_number = int(phone[1:])  # Убираем знак '+' и делаем str -> int
    except ValueError:
        return False
    else:
        if int_number >= 70000000000 and int_number <= 79999999999:
            return phone
    return False


def email_validator(email: str) -> str | bool:
    """Валидация емейла через регулярное выражение"""
    if re.fullmatch(REGEX, email):
        return email
    return False


async def json_validator(request: Request) -> dict | HTTPException:
    try:
        main_data = await request.json()
        return main_data
    except json.decoder.JSONDecodeError:
        raise HTTPException(status_code=404, detail="bad json")
