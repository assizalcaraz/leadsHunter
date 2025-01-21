import googlemaps
import os
import time
import random
from datetime import datetime

# Inicializa el cliente de Google Maps utilizando una clave desde las variables de entorno
gmaps = googlemaps.Client(key=os.getenv('GOOGLE_MAPS_API_KEY'))

def get_coordinates(city_name):
    """
    Obtiene las coordenadas de una ciudad utilizando el servicio de geocodificación de Google Maps.
    """
    try:
        print(f"Buscando coordenadas para la ciudad: {city_name}")
        geocode_result = gmaps.geocode(city_name)
        if geocode_result:
            location = geocode_result[0]['geometry']['location']
            print(f"Coordenadas encontradas: {location}")
            return f"{location['lat']},{location['lng']}"
        else:
            print(f"No se encontraron coordenadas para la ciudad: {city_name}")
            return None
    except Exception as e:
        print(f"Error obteniendo coordenadas para la ciudad {city_name}: {e}")
        return None

def google_places_search(query, location, radius):
    """
    Realiza una búsqueda de lugares en Google Places API.
    """
    try:
        results = gmaps.places(query=query, location=location, radius=radius)
        places = results.get('results', [])
        return places
    except Exception as e:
        print(f"Error realizando la búsqueda: {e}")
        return []

def extract_place_details(place_id):
    """
    Extrae detalles de un lugar utilizando su place_id.
    """
    try:
        details = gmaps.place(place_id=place_id)
        result = details.get('result', {})
        name = result.get('name', '')
        address = result.get('formatted_address', '')
        website = result.get('website', '')
        phone_number = result.get('formatted_phone_number', '')
        social_media = ''
        return name, address, website, phone_number, social_media
    except Exception as e:
        print(f"Error extrayendo detalles para el place_id {place_id}: {e}")
        return '', '', '', '', ''

def rate_limit():
    """
    Implementa un retraso aleatorio para evitar superar los límites de la API.
    """
    delay = random.uniform(1, 2)
    print(f"Esperando {delay:.2f} segundos para respetar los límites de la API...")
    time.sleep(delay)
