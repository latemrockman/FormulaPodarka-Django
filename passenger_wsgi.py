import os, sys
sys.path.insert(0, '/var/www/u1714561/data/www/meshkov-aa.ru/formula_podarka')
sys.path.insert(1, '/var/www/u1714561/data/djangosite/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'formula_podarka.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
