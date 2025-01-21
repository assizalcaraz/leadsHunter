import os
from celery import shared_task
import googlemaps
from .models import Place
from .utils import get_coordinates, google_places_search, extract_place_details


# Obtén la clave API de las variables de entorno
API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')

if not API_KEY:
    raise ValueError("La clave API de Google Maps no está configurada en las variables de entorno.")

# Inicializa el cliente de Google Maps
gmaps = googlemaps.Client(key=API_KEY)

@shared_task
def search_google_places(keywords, city, distance):
    try:
        # Obtener coordenadas de la ciudad
        location = get_coordinates(city)
        if not location:
            print(f"Error: No se pudieron obtener coordenadas para la ciudad {city}")
            return
        
        print(f"Iniciando búsqueda en Google Places con ubicación: {location}")
        queries = keywords.split(",")
        for query in queries:
            print(f"Buscando lugares para: {query}")
            # Realiza la búsqueda en Google Places
            places = google_places_search(query, location=location, radius=int(distance) * 1000)
            print(f"Resultados encontrados: {len(places)}")
            for place in places:
                # Guarda los resultados en la base de datos
                place_id = place.get('place_id')
                name, address, website, phone_number, social_media = extract_place_details(place_id)
                Place.objects.create(
                    name=name,
                    address=address,
                    website=website,
                    phone_number=phone_number,
                    social_media=social_media,
                    query=query,
                    map_url=f"https://www.google.com/maps/place/?q=place_id:{place_id}"
                )
    except Exception as e:
        print(f"Error en la tarea de búsqueda: {e}")


def get_coordinates(city):
    """
    Implementa la lógica para obtener coordenadas utilizando Google Maps Geocoding API.
    """
    try:
        geocode_result = gmaps.geocode(city)
        if geocode_result:
            location = geocode_result[0]['geometry']['location']
            return f"{location['lat']},{location['lng']}"
        else:
            print(f"No se encontraron coordenadas para la ciudad: {city}")
            return None
    except Exception as e:
        print(f"Error obteniendo coordenadas para la ciudad {city}: {e}")
        return None
