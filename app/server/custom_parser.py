from fastapi import HTTPException
from .validators import date_validator, phone_validator, email_validator


def parse_and_validate_fields(data: dict) -> dict[str, str] | HTTPException:
    """Проверка полей на валидность их названий,
    с одновременной валидацией значений, на случай если не
    найдется форма в mongo, добавляется тип поля к значению, что
    бы вернуть тип поля по ТЗ"""
    if data:
        valid_data = dict()

        for key, value in data.items():
            if "date" in key:
                if date_validator(value):
                    valid_data.update({"date": key})
                continue
            elif "phone" in key:
                if phone_validator(value):
                    valid_data.update({"phone": key})
                continue
            elif "email" in key:
                if email_validator(value):
                    valid_data.update({"email": key})
                continue
            elif "text" in key:
                valid_data.update({"text": key})
        if valid_data:
            return valid_data
    raise HTTPException(
        status_code=412, detail="Пустой запрос или не содержит валидных полей"
    )
