# Setup:

## install Django 2.2.15 and Pillow:
`pip install -r requirements.txt`<br>
\- or -<br>
`pipenv sync`<br>

## Populate database with initial data:
`python manage.py migrate users`<br>
`python manage.py migrate store`<br>
`python manage.py migrate`<br>
`python manage.py loaddata store/fixtures/banners.json`<br>
`python manage.py loaddata store/fixtures/brands.json`<br>
`python manage.py loaddata store/fixtures/items.json`<br>
`python manage.py loaddata users/fixtures/users.json`<br>

### User logins and passwords in `user_data.txt`

#### Few tests are available:
`python manage.py test`