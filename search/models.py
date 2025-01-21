from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    social_media = models.TextField(blank=True, null=True)
    query = models.CharField(max_length=255)
    map_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or "Unnamed Place"

class SearchResult(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    website = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    social_media = models.TextField(blank=True, null=True)
    query = models.CharField(max_length=255)
    map_url = models.URLField()

    def __str__(self):
        return self.name