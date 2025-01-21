FROM python:3.9-slim
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Asegura que el directorio raíz esté en el PYTHONPATH
ENV PYTHONPATH=/app

CMD ["gunicorn", "leadsHunter.wsgi:application", "--bind", "0.0.0.0:8001"]

#Celery
RUN adduser --disabled-password celeryuser
USER celeryuser
