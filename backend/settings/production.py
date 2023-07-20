from .base import *
import dj_database_url

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT', cast=int)
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Social Circle < tom.smith.4273@gmail.com>'
DOMAIN = env("DOMAIN")

DATABASES = {
    "default": dj_database_url.parse(env("DATABASE_URL"))
}