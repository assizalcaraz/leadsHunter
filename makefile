# Makefile para LeadsHunter

# Variables
COMPOSE_DEV = docker-compose -f docker-compose.dev.yaml
COMPOSE_PROD = docker-compose -f docker-compose.yaml

# Desarrollo
dev:
	$(COMPOSE_DEV) up --build -d

stop-dev:
	$(COMPOSE_DEV) down

logs-dev:
	$(COMPOSE_DEV) logs -f

sh-dev:
	$(COMPOSE_DEV) exec web sh

run-dev:
	$(COMPOSE_DEV) exec web python manage.py runserver 0.0.0.0:8000

migrate-dev:
	$(COMPOSE_DEV) exec web python manage.py migrate

createsuperuser-dev:
	$(COMPOSE_DEV) exec web python manage.py createsuperuser

collectstatic-dev:
	$(COMPOSE_DEV) exec web python manage.py collectstatic --noinput

test-dev:
	$(COMPOSE_DEV) exec web python manage.py test

# Producción
prod:
	$(COMPOSE_PROD) up --build -d

stop-prod:
	$(COMPOSE_PROD) down

logs-prod:
	$(COMPOSE_PROD) logs -f

sh-prod:
	$(COMPOSE_PROD) exec web sh
