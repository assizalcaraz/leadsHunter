# leadsHunter/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Establece la configuración predeterminada de Django para Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'leadsHunter.settings')

app = Celery('leadsHunter')

# Lee la configuración desde el archivo settings.py de Django.
# Todas las configuraciones de Celery deben estar prefijadas por "CELERY_".
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descubre automáticamente las tareas de todas las aplicaciones registradas en INSTALLED_APPS.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
