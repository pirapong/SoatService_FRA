import os
import sys

# Add your project directory to the sys.path
sys.path.append('/home/test/SoatService_FRA')

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Get the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

