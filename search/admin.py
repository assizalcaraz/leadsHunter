from django.contrib import admin
from .models import SearchResult, Place

# Registro de los modelos
@admin.register(SearchResult)
class SearchResultAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "query", "map_url")  # Campos que deseas mostrar en el listado
    search_fields = ("name", "address", "query")  # Campos que se pueden buscar
    list_filter = ("query",)  # Filtros en la barra lateral


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "website", "phone_number", "query", "map_url")
    search_fields = ("name", "address", "website", "phone_number")
    list_filter = ("query",)
