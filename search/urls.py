from django.urls import path
from .views import export_places, search_view

urlpatterns = [
    path('export/<str:format>/', export_places, name='export_places'),
    path('', search_view, name='search'),
]
