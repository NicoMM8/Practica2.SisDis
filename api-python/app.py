# Importamos Flask para manejar la aplicación web y jsonify para estructurar respuestas JSON.
from flask import Flask, jsonify

# Importamos SQLAlchemy para gestionar la base de datos en Flask.
from flask_sqlalchemy import SQLAlchemy

# Cargamos la configuración desde un archivo externo.
import config

# Inicializamos la aplicación Flask
app = Flask(__name__)

# Carga la configuración definida en config.py (por ejemplo, conexión a la base de datos).
app.config.from_object(config)

# Inicializa SQLAlchemy con la aplicación Flask para la gestión de la base de datos.
db = SQLAlchemy(app)

# Modelo de usuario para la base de datos con una tabla 'User'.
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # ID único como clave primaria.
    nombre = db.Column(db.String(50), nullable=False)  # Nombre con una restricción de que no puede ser nulo.

# Manejo de error de archivo
@app.route('/error-file')
def error_file():
    try:
        # Se intenta abrir un archivo inexistente para forzar un error.
        with open('archivo_inexistente.txt', 'r') as file:
            contenido = file.read()
        return jsonify({"message": contenido})  # Si el archivo existe (lo cual no ocurrirá), devuelve el contenido.
    except FileNotFoundError as e:
        # Capturamos la excepción de archivo no encontrado y respondemos con un JSON estructurado.
        return jsonify({
            "code": 404,
            "technicalMessage": str(e),
            "userMessage": "El archivo solicitado no se encontró."
        }), 404

# Manejo de error en la base de datos
@app.route('/error-db')
def error_db():
    try:
        # Se intenta obtener el primer usuario en la tabla 'User'.
        user = User.query.first()
        if user:
            return jsonify({"user": user.nombre})  # Si se encuentra el usuario, se retorna su nombre.
        else:
            return jsonify({"mensaje": "No se encontró ningún usuario."})  # Si no hay registros, se informa.
    except Exception as e:
        # Captura cualquier excepción no manejada en el acceso a la base de datos y la retorna en formato JSON.
        return jsonify({
            "code": 500,  # Código de error estándar para errores internos del servidor.
            "technicalMessage": str(e),
            "userMessage": "Error al acceder a la base de datos. Por favor, inténtelo más tarde."
        }), 500

# Importamos requests para hacer llamadas a APIs externas.
import requests

# Manejo de error en llamadas a APIs externas
@app.route('/error-external')
def error_external():
    try:
        # Se fuerza un error apuntando a una URL errónea o simulando un timeout.
        response = requests.get("http://pokeapi.co/api/v2/pokemon/invalid_endpoint", timeout=3)
        response.raise_for_status()  # Lanza un error si el código de estado no es 200 (OK).
        return jsonify({"data": response.json()})  # Si el servidor responde correctamente, se retorna la respuesta JSON.
    except requests.exceptions.RequestException as e:
        # Captura cualquier error en la conexión y lo devuelve en formato JSON estructurado.
        return jsonify({
            "code": 502,  # Código de error usado para problemas en comunicaciones con servidores externos.
            "technicalMessage": str(e),
            "userMessage": "Error en la llamada a la API externa, intenta de nuevo más tarde."
        }), 502

# Manejador global de excepciones
@app.errorhandler(Exception)
def handle_global_exception(e):
    # Se puede registrar el error aquí para depuración (logging recomendado).
    response = jsonify({
        "code": 550,  # Código arbitrario para errores inesperados. Generalmente, 500 es estándar.
        "technicalMessage": str(e),
        "userMessage": "Ha ocurrido un error inesperado. Por favor, inténtelo de nuevo más tarde."
    })
    response.status_code = 550
    return response

# Inicio de la aplicación Flask
if __name__ == '__main__':
    # Se ejecuta la aplicación en modo desarrollo con la opción debug activada.
    # Se configura la aplicación para que acepte conexiones desde cualquier IP (0.0.0.0).
    app.run(host="0.0.0.0", port=5000, debug=True)

