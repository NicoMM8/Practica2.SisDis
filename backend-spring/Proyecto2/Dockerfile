# Dockerfile para la aplicación Spring Boot
FROM openjdk:11-jre-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo JAR de la aplicación; asegúrate de haberlo construido previamente (por ejemplo, con Maven)
COPY target/Practica-2.jar Practica-2.jar

# Exponemos el puerto en el que se ejecutará la aplicación (en este ejemplo, 8090)
EXPOSE 8090

# Comando para ejecutar la aplicación
CMD ["java", "-jar", "Practica-2.jar"]
