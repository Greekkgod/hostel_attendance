"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

_application = get_wsgi_application()

def handler(request, context):
    """Vercel serverless function handler"""
    return _application(request.environ, request.start_response)

# Also keep these for compatibility
application = _application
app = _application
