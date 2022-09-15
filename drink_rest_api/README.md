social media template from https://github.com/tomitokko/django-social-media-website/blob/main/core/views.py



don't use npm i bcrypt, it wont work


To get second database
1. Have to use pip install bcrypt
2. In psql, create database users_api
3. To migrate second database: python manage.py migrate --database=users
4. Run python manage.py sqlmigrate users_api 0001