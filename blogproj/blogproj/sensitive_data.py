SECRET_KEY = 'r&iy)3a%^uj0ja50yvx0qot%+*o(xe=p*ec1ofkevvf9#^c^x7'
DEBUG = True
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'kodland',
        'USER': 'kodland',
        'PASSWORD': 'kodland',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}