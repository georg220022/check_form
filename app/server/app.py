from fastapi import Request, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from .custom_parser import parse_and_validate_fields
from .validators import json_validator
from form_data import form_data


async def add_test_data(request: Request) -> dict[str, str]:
    mongo_client: AsyncIOMotorClient = request.app.state.mongo_client["forms_json_db"]
    data = await mongo_client.json_forms.find({}).to_list(length=10)
    if not data:
        await mongo_client.json_forms.insert_many(form_data)
        return {"ok": "Данные успешно загружены"}
    return {"error": "Данные уже есть, 2-й раз загружать не нужно."}


async def search_form(request: Request) -> dict[str, str] | HTTPException:
    mongo_client: AsyncIOMotorClient = request.app.state.mongo_client["forms_json_db"]
    main_data: dict | HTTPException = await json_validator(
        request
    )  # Получаем данные из тела запроса
    if not main_data:  # Если тела нет, пытаемся получить из query_params
        main_data = dict(request.query_params)
    valid_data: dict[str, str] | HTTPException = parse_and_validate_fields(main_data)
    filter_data = valid_data.copy()
    filter_data.update(dict(length_form=len(valid_data)))
    result = await mongo_client.json_forms.find_one(
        filter_data, {"_id": False, "length_form": False}
    )
    if not result:  # Если форма не найдена, возвращаем типы полей
        result = {v: k for k, v in valid_data.items()}
        return result
    return {"name": result["name"]}
