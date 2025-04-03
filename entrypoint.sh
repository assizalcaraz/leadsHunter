#!/bin/bash

echo "Esperando a la base de datos..."
while ! nc -z "$DB_HOST" "$DB_PORT"; do
  sleep 1
done
echo "Base de datos lista. Ejecutando migraciones..."

python manage.py makemigrations
python manage.py migrate

echo "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
User.objects.filter(username='admin').exists() or \
User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')" | python manage.py shell

# Arrancar el servidor de desarrollo
exec python manage.py runserver 0.0.0.0:8000
