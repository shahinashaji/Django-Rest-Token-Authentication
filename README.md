# Django-Rest-Token-Authentication

#### Create Virtual Environment:
```bash 
    python -m venv env 
```

#### Activate Virtual Environment:
    env\Scripts\activate

#### Django:
    pip install django

#### Django Rest:
    pip install djangorestframework

#### Add this snippet in settings.py to enable authentication
```
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        ],
    }
```
#### Create superuser:
    python manage.py createsuperuser

#### Install Pytz

    pip install pytz

## Notes

=> Check on the screenshots available in the repo to see the requests.

=> [Reference Link]: https://www.geeksforgeeks.org/jwt-authentication-with-django-rest-framework/