from .base import *


DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'twinravens',
       'USER': 'twinravens',
       'PORT': '5432'
   }
}