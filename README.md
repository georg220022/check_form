### Form Check
##### Требования для запуска: Docker  
##### Технологии: FastApi, Python3, Docker, Mongo, Uvicorn  
##### Описание:  
Поля считаются валидными если их имя содержит в себе слово "date", "phone", "email", "text".  
Например:  
{"qqqaaaemail": "1@1.ru}" или {"email": "1@1.ru}" Валидно.  
{"qqqaaae_mail": "1@1.ru}" или {"pochta": "1@1.ru"} НЕ валидно.  
  
Поле email формата "x@x.x"  
Поле date принимает дату только в форматах DD.MM.YYYY или YYYY-MM-DD  
Поле phone принимает только РФ номера телефонов в формате "+71234567890"  
Поле text не валидируется  
  
Присылать данные можно либо в json POST запроса, либо в строке запроса (query_params)  
  
#### Запуск:  
1) Клонировать репозиторий  
2) Перейти в папку проекта, поднять докер: docker-compose up  
3) Для заполнения Mongo данными, вставить в строку браузера(GET запрос): http://localhost:8000/add_test_data  
#### Запустить тестовые запросы:  
4.1) Выполнить docker container ls, копировать CONTAINER_ID контейнера web  
4.2) Выполнить docker exec -it 'сюда вставить CONTAINER_ID' bash  
4.3) Выполнить python3 test_request.py  
  
Пример:  
![Иллюстрация к проекту](https://github.com/georg220022/check_form/blob/main/img/2.png)

