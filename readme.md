#Учет наноматериалов

Пробная система.


Использует Django 2.2. и Python 3.5


Установка зависимостей:

    pip install -r requirements.txt


Первый старт:

    python manage.py migrate

Это для создания базы.

Потом

    python manage.py createsuperuser

Потом запускаем дев сервер:

    python manage.py runserver

В браузере открываем:

    127.0.0.1:8000/admin

Вводим логин и пароль ранее созданного суперпользователя.
Можно попробовать повносить данные.
