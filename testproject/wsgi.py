"""
WSGI config for testproject project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testproject.settings')

application = get_wsgi_application()

# Handlers for different platforms
app = application  # For Vercel
# For Render, the application variable is used directly
