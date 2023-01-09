# Форма для заполнения MongoDB
form_data = [
    dict(
        name="my_form",
        length_form=4,
        email="my_email",
        date="my_date",
        phone="my_phone",
        text="texted",
    ),
    dict(
        name="admin_form",
        length_form=4,
        email="admin_email",
        date="admin_date",
        phone="admin_phone",
        text="text",
    ),
    dict(
        name="director_form",
        length_form=4,
        email="my_email_director",
        date="date",
        phone="phones",
        text="text_custom",
    ),
    dict(
        name="banned_form",
        length_form=4,
        email="banned_email",
        date="date",
        phone="phone",
        text="text",
    ),
    dict(
        name="user_form",
        length_form=3,
        email="user_email",
        date="user_date",
        text="text_user",
    ),
    dict(
        name="winner_form",
        length_form=3,
        email="winner_email",
        date="date",
        phone="phone",
    ),
    dict(
        name="loser_form",
        length_form=3,
        email="loser_email",
        phone="loser_phone",
        text="text",
    ),
    dict(
        name="leader_form",
        length_form=3,
        email="leader_email",
        phone="leader_phone",
        text="text",
    ),
    dict(
        name="default_form_4_field",
        length_form=4,
        email="email",
        date="date",
        phone="phone",
        text="text",
    ),
    dict(
        name="default_form_3_field",
        length_form=3,
        email="email",
        date="date",
        text="text",
    ),
    dict(
        name="default_form_2_field",
        length_form=2,
        email="email",
        phone="phone"
    ),
    dict(
        name="default_form_1_field",
        length_form=1,
        email="email"
    ),
]

# Форма с не валидными данными для запроса
not_valid_data = [
    dict(email="admin.ru"),
    dict(email="test@test"),
    dict(email="test@test",
         phone="+791235124214"),
]

# Не существующие формы с валидными данными для запроса
not_found_form = [
    dict(news_email="1@1.ru",
         args_date="01.01.2022"),
    dict(mmmemail="1@1.ru",
         ddddate="10.01.2022",
         ttext="just text"),
    dict(unknown_email="1@1.ru")
]

# Существующие формы с валидными данными для запроса
good_data = [
    dict(
        my_email="1@1.ru",
        my_date="01.02.2022",
        my_phone="+78886665544",
        texted="just text",
    ),
    dict(
         admin_email="1@1.ru",
         admin_date ="01.02.2022",
         admin_phone ="+78886665544",
         text ="just text",
    ),
    dict(
         my_email_director ="1@1.ru",
         date ="01.02.2022",
         phones ="+78886665544",
         text_custom ="just text",
    ),
    dict(
         banned_email="1@1.ru" ,
         date ="01.02.2022",
         phone ="+78886665544",
         text ="just text",
    ),
    dict(
         user_email="1@1.ru" ,
         user_date ="01.02.2022",
         text_user ="just text",
    ),
    dict(
         winner_email="1@1.ru" ,
         date ="01.02.2022",
         phone ="+78886665544",
    ),
    dict(
         loser_email ="1@1.ru",
         loser_phone ="+78886665544",
         text ="just text",
    ),
    dict(
         leader_email ="1@1.ru",
         leader_phone ="+78886665544",
         text ="just text",
    ),
    dict(
         email ="1@1.ru",
         date ="01.02.2022",
         phone ="+78886665544",
         text ="just text",
    ),
    dict(
         email ="1@1.ru",
         date ="01.02.2022",
         text ="just text",
    ),
    dict(
         email ="1@1.ru",
         phone ="+78886665544",
    ),
    dict(
         email ="1@1.ru",
    )
]
