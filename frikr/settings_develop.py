# -*- coding: utf-8 -*-
from settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db_DEVELOP.sqlite3'),
    }
}

EMAIL_HOST = 'localhost'
EMAIL_PORT = '1025'