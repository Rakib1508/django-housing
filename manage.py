import os
import sys
import dotenv


def main():
    """Run administrative tasks."""
    dotenv.read_dotenv()
    server_mode = os.environ.get('SERVER_MODE', None)
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
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
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
