import os

from django.core.wsgi import get_wsgi_application

server_mode = os.environ.get('SERVER_MODE', None)
print('server mode', server_mode)

if server_mode == 'development':
    print('Using development settings')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.development_settings')
elif server_mode == 'production':
    print('Using production settings')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.production_settings')
else:
    print('Using fallback settings')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.fallback_settings')

application = get_wsgi_application()
