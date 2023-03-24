"""
ASGI config for barragens project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'barragens.settings')
os.environ.setdefault('DB_NAME', 'default')
os.environ.setdefault('DB_USER', 'alvar')
os.environ.setdefault('DB_PASSWORD', '123')
os.environ.setdefault('DB_HOST', 'localhost')
os.environ.setdefault('DB_PORT', '3306')

application = get_asgi_application()
