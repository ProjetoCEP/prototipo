from decouple import config


SECRET_KEY = config('SECRET_KEY', 'secret-key')
DEBUG = config('DEBUG', default=False, cast=bool)
