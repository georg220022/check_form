import requests
from form_data import not_valid_data, not_found_form, good_data

good_name_form = [
    "my_form",
    "admin_form",
    "director_form",
    "banned_form",
    "user_form",
    "winner_form",
    "loser_form",
    "leader_form",
    "default_form_4_field",
    "default_form_3_field",
    "default_form_2_field",
    "default_form_1_field",
]


for i in range(0, len(good_data) - 1):
    if i <= 2:
        req = requests.post("http://0.0.0.0:8000/get_form", json=not_found_form[i])
        print("[OK]    Форма валидна, но не найдена: ", req.text)
        req = requests.post("http://0.0.0.0:8000/get_form", json=not_valid_data[i])
        print("[OK]    Не валидные данные в форме: ", req.text)
    req = requests.post("http://0.0.0.0:8000/get_form", json=good_data[i])
    if good_name_form[i] in req.text:
        print("[OK]    Найдена форма: ", good_name_form[i])
    else:
        print("[FALSE!!!]    ", good_name_form[i], " форма не найдена")
