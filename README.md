# LeadsHunter

LeadsHunter es una aplicación Django diseñada para la búsqueda y gestión eficiente de lugares mediante palabras clave, ciudades y distancias. El proyecto utiliza Docker para la virtualización y Nginx como servidor de archivos estáticos y proxy inverso. Está configurado para integrarse fácilmente con RabbitMQ para tareas asíncronas utilizando Celery.

## Características

- **Gestión de búsquedas:** Permite buscar lugares a través de palabras clave, ciudad y distancia.
- **Despliegue en contenedores:** Configuración completa usando Docker Compose para garantizar portabilidad y consistencia.
- **Procesamiento asíncrono:** Integración con Celery y RabbitMQ para manejar tareas largas o en segundo plano.
- **Nginx como proxy inverso:** Maneja el enrutamiento de solicitudes y sirve archivos estáticos.
- **PostgreSQL como base de datos:** Configuración optimizada para entornos de producción.

---

## Requisitos previos

- Docker (v20.10 o superior)
- Docker Compose (v2.29.0 o superior)
- Python 3.9+
- Git

---

## Configuración e instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/tu-usuario/leadshunter.git
   cd leadshunter
   ```

2. **Crear un archivo `.env` en la raíz del proyecto:**

   ```env
   POSTGRES_USER=usuario
   POSTGRES_PASSWORD=contraseña
   POSTGRES_DB=leads_hunter
   RABBITMQ_USER=usuario
   RABBITMQ_PASSWORD=contraseña
   DEBUG=True
   ```

3. **Construir y ejecutar los contenedores:**

   ```bash
   docker compose up --build -d
   ```

4. **Recopilar los archivos estáticos:**

   Ejecutar el comando desde el contenedor `web`:

   ```bash
   docker compose exec web python manage.py collectstatic
   ```

5. **Acceso a la aplicación:**

   La aplicación estará disponible en: [http://localhost:8080](http://localhost:8080)

---

## Estructura del proyecto

```plaintext
leadshunter/
├── Dockerfile               # Configuración del contenedor web
├── docker-compose.yaml      # Configuración de servicios con Docker Compose
├── .env                     # Variables de entorno (no se incluye en el repo)
├── leadsHunter/             # Proyecto Django principal
├── search/                  # Aplicación interna de búsqueda
├── nginx/
│   └── nginx.conf           # Configuración de Nginx
├── static/                  # Archivos estáticos
├── media/                   # Archivos subidos por el usuario
└── requirements.txt         # Dependencias de Python
```

---

## Servicios principales

1. **Web:** Servidor Gunicorn que ejecuta la aplicación Django.
2. **Base de datos:** PostgreSQL para almacenamiento de datos.
3. **Mensajería:** RabbitMQ para manejar tareas asíncronas con Celery.
4. **Servidor proxy:** Nginx para servir archivos estáticos y manejar el enrutamiento de solicitudes.

---

## Comandos útiles

- **Levantar los servicios:**
  ```bash
  docker compose up -d
  ```

- **Detener los servicios:**
  ```bash
  docker compose down
  ```

- **Ejecutar migraciones de base de datos:**
  ```bash
  docker compose exec web python manage.py migrate
  ```

- **Crear un superusuario:**
  ```bash
  docker compose exec web python manage.py createsuperuser
  ```

---

## Problemas comunes y soluciones

1. **Los estilos no se aplican:**
   - Asegúrate de haber ejecutado `collectstatic`.
   - Verifica la configuración de Nginx para los archivos estáticos.

2. **Conexión fallida con PostgreSQL:**
   - Revisa las variables de entorno en el archivo `.env`.
   - Verifica que el servicio de base de datos esté corriendo.

3. **RabbitMQ no se conecta:**
   - Asegúrate de que el usuario y contraseña de RabbitMQ en el archivo `.env` sean correctos.

---

## Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras algún problema o deseas agregar nuevas funcionalidades, no dudes en crear un [issue](https://github.com/tu-usuario/leadshunter/issues) o enviar un pull request.

---

## Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).
```

Copia y pega este texto directamente en tu archivo `README.md`. Asegúrate de reemplazar los enlaces y configuraciones específicas según sea necesario.