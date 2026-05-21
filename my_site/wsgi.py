import os
from django.core.wsgi import get_wsgi_application

# Estableix el mòdul de configuració per defecte de Django per al programa
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_site.settings")

# Retorna l'aplicació WSGI avalada per Django per a la comunicació amb el servidor web
application = get_wsgi_application()