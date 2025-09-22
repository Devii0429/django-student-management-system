import os

if os.environ.get('DJANGO_ENV') == 'production':
    from .settings.production import *
else:
    from .settings.local import *