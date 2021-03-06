import os
from django.core.wsgi import get_wsgi_application
from config.environment import SETTINGS_MODULE
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_MODULE)
application = get_wsgi_application()
application = DjangoWhiteNoise(application)