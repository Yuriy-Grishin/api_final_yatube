## Описание проекта 

API для Yatube. 

Социалная сеть со следующими функциями: публикация постов и комментариев, подписка на авторов.
Доступна работа со следующими методами: GET, POST, PATCH, DELETE, PUT.
Доступна поддержка данных в формате JSON и аутентификация по JWT-токену.
Используемые программы: Python, Django REST Framework.
Для управления версиями используется git

## Примеры запросов к API
Получаем список групп: GET api/v1/groups/

Получаем список постов: GET api/v1/posts/

Получаем комментарии: GET api/v1/{post_id}/comments/

Создаем пост: POST /api/v1/posts/

Обновляем пост: PUT /api/v1/posts/{id}/

Получаем JWT-токен (Joser): POST /api/v1/jwt/create/

## Стек технологий
Python;
Django;
Django REST framework;
DRF Simple JWT

## Как запустить проект
Клонировать репозиторий и перейти в него в командной строке:
git clone https://github.com/Yuriy-Grishin/api_final_yatube.git

Cоздать и активировать виртуальное окружение:
python -m venv env
source env/bin/activate
python -m pip install --upgrade pip

Установить зависимости из файла requirements.txt:
pip install -r requirements.txt

Выполнить миграции:
python manage.py migrate

Запустить проект:
python manage.py runserver


