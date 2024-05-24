pip install virtualenv

python -m venv payenv

payenv\Scripts\activate

pip install django

python manage.py migrate

python manage.py runserver
