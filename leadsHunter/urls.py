from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from search.views import export_places

urlpatterns = [
    path("admin/", admin.site.urls),
    path("search/", include("search.urls")),
    path('export/<str:format>/', export_places, name='export_places'),

]

# Servir archivos estáticos en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


