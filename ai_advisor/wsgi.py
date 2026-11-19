"""
WSGI config for AI Advisor project.
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_advisor.settings')
application = get_wsgi_application()
