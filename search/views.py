from django.shortcuts import render
from django.http import HttpResponse
from .models import Place  # Cambiar SearchResult por Place
from .tasks import search_google_places
import csv
import random
import time
from io import BytesIO
import pandas as pd
from .utils import get_coordinates, google_places_search, extract_place_details

def search_view(request):
    """
    Vista para iniciar una nueva búsqueda.
    """
    if request.method == "POST":
        keywords = request.POST.get("keywords")
        city = request.POST.get("city")
        distance = request.POST.get("distance")

        # Depuración
        print(f"Ciudad recibida: {city}")
        print(f"Palabras clave: {keywords}")
        print(f"Distancia: {distance}")

        # Llama a la tarea de Celery para realizar la búsqueda
        search_google_places.delay(keywords, city, distance)

        # Redirige al usuario a la página de resultados
        return redirect("search_results")

    # Renderiza el formulario para una nueva búsqueda
    return render(request, "maps_finder/search.html")


def search_results_view(request):
    """
    Vista para mostrar los resultados de búsqueda almacenados.
    """
    # Carga los resultados disponibles desde la base de datos
    results = Place.objects.all().order_by("-id")[:50]

    # Renderiza la página de resultados
    return render(request, "maps_finder/search_results.html", {"results": results})


def finder(keywords, city, distance):
    """
    Realiza una búsqueda manual utilizando las funciones de Google Places.
    Guarda los resultados en la base de datos.
    """
    location = get_coordinates(city)
    if not location:
        print("No se pudo obtener la ubicación para la ciudad especificada.")
        return []

    queries = [keyword.strip() for keyword in keywords.split(",")]
    all_results = []

    for query in queries:
        print(f"Realizando búsqueda para: {query}")
        places = google_places_search(query, location=location, radius=int(distance) * 1000)

        for place in places:
            place_id = place.get('place_id', 'N/A')
            name, address, website, phone_number, social_media = extract_place_details(place_id)
            url = f"https://www.google.com/maps/place/?q=place_id:{place_id}"

            # Guardar en la base de datos
            place_obj = Place(
                name=name if name else None,
                address=address if address else None,
                website=website if website else None,
                phone_number=phone_number if phone_number else None,
                social_media=social_media if social_media else None,
                query=query,
                map_url=url
            )
            place_obj.save()

            all_results.append(place_obj)

        # Retraso aleatorio para evitar bloqueos
        delay = random.uniform(0.1, 0.5)
        print(f"Esperando {delay:.2f} segundos antes de la próxima búsqueda...")
        time.sleep(delay)

    return all_results

def export_places(request, format='csv'):
    """
    Exporta los lugares guardados en la base de datos en diferentes formatos (CSV, JSON, Excel).
    """
    places = Place.objects.all()

    if format == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="places.csv"'
        writer = csv.writer(response)
        writer.writerow(['Nombre', 'Dirección', 'Website', 'Teléfono', 'Redes Sociales', 'Consulta', 'Mapa URL'])

        for place in places:
            writer.writerow([place.name, place.address, place.website, place.phone_number, place.social_media, place.query, place.map_url])

        return response

    elif format == 'json':
        from django.core.serializers import serialize
        data = serialize('json', places)
        response = HttpResponse(data, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="places.json"'
        return response

    elif format == 'excel':
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="places.xlsx"'

        data = [{
            'Nombre': place.name,
            'Dirección': place.address,
            'Website': place.website,
            'Teléfono': place.phone_number,
            'Redes Sociales': place.social_media,
            'Consulta': place.query,
            'Mapa URL': place.map_url,
        } for place in places]

        df = pd.DataFrame(data)
        with BytesIO() as buffer:
            writer = pd.ExcelWriter(buffer, engine='xlsxwriter')
            df.to_excel(writer, index=False, sheet_name='Places')
            writer.save()
            buffer.seek(0)
            response.write(buffer.getvalue())

        return response

    else:
        return HttpResponse("Formato no soportado.", status=400)
