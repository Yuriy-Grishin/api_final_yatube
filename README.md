Описание: 
API для Yatube. Социалная сеть со следующими функциями: публикация постов и комментариев, подписка на авторов.


Установка: 
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
