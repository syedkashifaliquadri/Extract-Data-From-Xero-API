"""
WSGI config for CRUD_app_using_Django_PostgreSQL project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CRUD_app_using_Django_PostgreSQL.settings')

application = get_wsgi_application()
