# Dockerfile para la API de Python (Flask)
FROM python:3.9-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo de requerimientos e instalamos las dependencias
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto de la aplicación al directorio de trabajo
COPY . .

# Exponemos el puerto en el que correrá la API
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
