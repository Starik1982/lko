DEBUG = False
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'db1',
    'USER': 'lko',
    'PASSWORD': '1488',
    'HOST': 'localhost', # Set to empty string for localhost.
    'PORT': '', # Set to empty string for default.
    }
}
