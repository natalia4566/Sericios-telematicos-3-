FROM python:3.10-slim

# Crear directorio
WORKDIR /app

# Copiar archivos de la aplicación
COPY . /app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Instalar Gunicorn
RUN pip install gunicorn

# Crear carpeta para SSL
RUN mkdir -p /etc/ssl/app

# Exponer puertos
EXPOSE 8000

# Comando para iniciar Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "run:app"]
