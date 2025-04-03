from django.db import models

class Place(models.Model):
    name = models.CharField("Nombre", max_length=255, blank=True, null=True)
    address = models.TextField("Dirección", blank=True, null=True)
    website = models.URLField("Sitio Web", blank=True, null=True)
    phone_number = models.CharField("Teléfono", max_length=20, blank=True, null=True)
    social_media = models.TextField("Redes Sociales", blank=True, null=True)
    query = models.CharField("Consulta original", max_length=255)
    map_url = models.URLField("Enlace a Google Maps")
    zona = models.CharField("Zona o Ciudad", max_length=100, blank=True, null=True)
    radius_km = models.IntegerField("Radio de búsqueda (km)", blank=True, null=True)
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "address"],
                name="unique_place_name_address"
            )
        ]
        ordering = ['-created_at']

    def __str__(self):
        return self.name or "Lugar sin nombre"
