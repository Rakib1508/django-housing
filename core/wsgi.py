import os
from django.core.wsgi import get_wsgi_application


server_mode = os.environ.get('SERVER_MODE', None)

if server_mode == 'production':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.production_settings')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.development_settings')

application = get_wsgi_application()
