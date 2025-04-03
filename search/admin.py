from django.contrib import admin
from .models import Place

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "query", "zona", "radius_km", "created_at")
    search_fields = ("name", "address", "website", "phone_number")
    list_filter = ("query", "zona", "radius_km")



