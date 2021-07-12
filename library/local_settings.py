DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'library',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '',
    }
}
ALLOWED_HOSTS = ['https://kimmy-library.herokuapp.com', '127.0.0.1']
SECRET_KEY = 'nu2xx00wvzho4c43c667jwdgflo1nph#^^$1a6=oip&97852m4'