from __future__ import absolute_import, unicode_literals

# Importa el archivo con el nombre actualizado
from .celery_app import app as celery_app

__all__ = ('celery_app',)
