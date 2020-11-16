Для запуска выполните след шаги:
- склонируйте репозиторий
- запустите из корня проекта python pip install -r requirements.txt


- запустите из корня проекта python manage.py migrate
- создатей пользователя админа python manage.py createsuperuser 

- запустите из корня проекта  python manage.py runserver для запуска тестового сервера 



Описание приложения

В адресной строке:
- /admin - вход в админку
- /rest-auth/login -api авторизация
- /api - само api 

- /api/polls - получение всех опросов (для определенного ID: /api/polls/id/)
- /api/questions - получение всех вопросов
- /api/answers - получение всех ответов 
- /api/statistic/ - статистика

