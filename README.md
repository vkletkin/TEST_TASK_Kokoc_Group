Задание: Создать сервис прохождения опросов пользователями на Django.

    Обязательная часть:

        1. Можно зарегистрироваться и логинится. Наверху показано под каким логином ты зашел. (выполнено)
        2. Тесты и ответы на них создаются динамически через админку. (выполнено)
        3. Список тестов выводится в виде содержания произвольного вида (столбец, таблица, как удобно) (выполнено)

    Фронт делается с помощью шаблонизатора Django, СУБД произвольная

    Опция 1.

        1. За прохождение тестов начисляется какое-то количества валюты.
        2. Валюту можно потратить на перекрашивание рамки логина или бэкграунда на странице профиля.
        3. Показывать список пользователей и количество пройденных тестов на отдельной странице, там же показывать цветовую дифференциацию пользователей. (выполнено)

    Опция 2.

        1. Сделать фронт на реакте, в виде SPA или отдельных модулей.


    Выкатить на github, деплой не обязательно, проверим под режимом разработчика.
    
    
Запуск приложения на ОС Windows:

     Шаг 1) Установка и запуск вируального окружения , командами python -m venv venv,  source venv/Scripts/activate
     Шаг 2) Установка всех пакетов в файле requirements.txt, командой -m pip install -r requirements.txt 
     Шаг 3) Пропись миграций командами python manage.py makemigrations и python manage.py migrate.
     Шаг 4) Запуск сервера python manage.py runserver
