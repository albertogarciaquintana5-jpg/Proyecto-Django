# Proyecto Django - Centro Escolar

## Requisitos
- Python 3.10 o superior
- pip (gestor de paquetes de Python)
- Django 4.x o superior

## Instalación

1. Clona o descarga este repositorio en tu equipo.
2. Abre una terminal y navega a la carpeta principal del proyecto (donde está `manage.py`).
3. Instala las dependencias necesarias:

   ```bash
   pip install django
   ```

4. Realiza las migraciones de la base de datos:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. (Opcional) Crea un superusuario para acceder al panel de administración:

   ```bash
   python manage.py createsuperuser
   ```

## Ejecución del servidor

1. Desde la carpeta principal del proyecto, ejecuta:

   ```bash
   python manage.py runserver
   ```

2. Abre tu navegador y accede a [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Notas
- Para detener el servidor, presiona `Ctrl+C` en la terminal.
- Puedes acceder al panel de administración en [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) usando el superusuario creado.

---

Si tienes dudas, revisa la documentación oficial de Django: https://docs.djangoproject.com/es/
