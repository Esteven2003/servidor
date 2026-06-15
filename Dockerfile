# Usamos una imagen ligera de Python
FROM python:3.11-slim

# Creamos una carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiamos e instalamos las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código de nuestra app
COPY app.py .

# Exponemos el puerto de Flask
EXPOSE 5000

# Comando para arrancar la aplicación
CMD ["python", "app.py"]