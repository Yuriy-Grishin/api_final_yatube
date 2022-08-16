Описание.
API для Yatube. Социалная сеть со следующими функциями: публикация постов и комментариев, подписка на авторов.


Установка.
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


Примеры запросов к API.
Получаем список групп: GET api/v1/groups/
Получаем список постов: GET api/v1/posts/
Получаем комментарии: GET api/v1/{post_id}/comments/
Создаем пост: POST /api/v1/posts/
Обновляем пост: PUT /api/v1/posts/{id}/
Получаем JWT-токен (Joser): POST /api/v1/jwt/create/
