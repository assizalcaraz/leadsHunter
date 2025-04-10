### 🗓️ [FECHA] - [TÍTULO BREVE DEL CAMBIO]

- [Breve descripción del cambio 1]
- [Breve descripción del cambio 2]
- [Notas sobre migraciones, scripts ejecutados, decisiones importantes]
- [Indicadores de validación o testeo si aplican]


### 🗓️ 2025-04-03 - Refactor modelo Place y limpieza de duplicados

- Se eliminó el modelo `SearchResult`.
- Se agregó una restricción `UNIQUE(name, address)` en el modelo `Place`.
- Se añadieron los campos `zona` y `radius_km`.
- Se migró la base de datos con estas nuevas condiciones.
- Se realizó limpieza de registros duplicados desde la shell de Django.
- Se actualizó el `admin.py` para permitir filtrar y buscar por zona.
- Se verificó que los duplicados ya no se indexan.
- Se generó commit con todos los cambios estructurales y de datos.







#  Manual de uso del Makefile

Este documento describe los comandos disponibles en el `Makefile` y su propósito. Está pensado para facilitar el uso diario durante el desarrollo y despliegue del proyecto **leadsHunter**.

## 📁 Alias definidos en el Makefile

### 🛠️ Desarrollo

- `make dev`: Levanta todos los servicios en entorno de desarrollo usando:
  ```bash
  docker-compose -f docker-compose.dev.yaml up --build
  ```

- `make stop-dev`: Detiene los servicios de desarrollo:
  ```bash
  docker-compose -f docker-compose.dev.yaml down
  ```

- `make logs-dev`: Muestra los logs en tiempo real:
  ```bash
  docker-compose -f docker-compose.dev.yaml logs -f
  ```

- `make sh-dev`: Abre una shell dentro del contenedor `web` en desarrollo:
  ```bash
  docker-compose -f docker-compose.dev.yaml exec web sh
  ```

- `make run-dev`: Ejecuta el servidor Django de desarrollo manualmente dentro del contenedor:
  ```bash
  docker-compose -f docker-compose.dev.yaml exec web python manage.py runserver 0.0.0.0:8000
  ```

- `make migrate-dev`: Ejecuta las migraciones de Django:
  ```bash
  docker-compose -f docker-compose.dev.yaml exec web python manage.py migrate
  ```

- `make createsuperuser-dev`: Crea un superusuario:
  ```bash
  docker-compose -f docker-compose.dev.yaml exec web python manage.py createsuperuser
  ```

- `make test-dev`: Ejecuta los tests definidos para el entorno de desarrollo:
  ```bash
  docker-compose -f docker-compose.dev.yaml exec web python manage.py test
  ```

### 🚀 Producción

- `make prod`: Levanta los servicios en entorno de producción:
  ```bash
  docker-compose -f docker-compose.yaml up --build
  ```

- `make stop-prod`: Detiene los servicios de producción:
  ```bash
  docker-compose -f docker-compose.yaml down
  ```

- `make logs-prod`: Muestra los logs de producción:
  ```bash
  docker-compose -f docker-compose.yaml logs -f
  ```

- `make sh-prod`: Abre una shell en el contenedor `web` de producción:
  ```bash
  docker-compose -f docker-compose.yaml exec web sh
  ```

## ✅ Recomendaciones

- Usar `make dev` para trabajar localmente.
- Verificar que todo funcione bien en `dev` antes de hacer merge con `prod`.
- Recordar usar `make migrate-dev` y `make createsuperuser-dev` luego de modificar modelos o al iniciar el entorno.

---

Este archivo puede expandirse con nuevas tareas frecuentes. Sentite libre de agregar comandos que te faciliten el trabajo.

