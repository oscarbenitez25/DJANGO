from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Rutes del projecte (URL patterns)
urlpatterns = [
    # Ruta per accedir al panell d'administració de Django
    path("admin/", admin.site.urls),
    
    # Inclou les rutes de l'aplicació "blog" a l'arrel del lloc web
    path("", include("blog.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Serveix arxius multimèdia en desenvolupament

# Controlador per a l'error de pàgina no trobada (Error 404)
handler404 = "blog.views.custom_404"