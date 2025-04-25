# app.py
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
# Carga la configuración definida en config.py
app.config.from_object(config)

# Inicializa SQLAlchemy con la aplicación Flask
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

@app.route('/error-file')
def error_file():
    try:
        # Intentamos abrir un archivo que no existe para provocar la excepción.
        with open('archivo_inexistente.txt', 'r') as file:
            contenido = file.read()
        # Si por alguna razón el archivo se abre (lo cual no sucederá), se retorna su contenido.
        return jsonify({"message": contenido})
    except FileNotFoundError as e:
        # Capturamos la excepción y devolvemos la respuesta en formato JSON.
        return jsonify({
            "code": 404,
            "technicalMessage": str(e),
            "userMessage": "El archivo solicitado no se encontró."
        }), 404

# Ruta de ejemplo para simular una consulta a la base de datos y capturar errores
@app.route('/error-db')
def error_db():
    try:
        # Simula una consulta a la base de datos
        user = User.query.first()
        if user:
            return jsonify({"user": user.nombre})
        else:
            return jsonify({"mensaje": "No se encontró ningún usuario."})
    except Exception as e:
        # Retorna un JSON con el mensaje del error y un código de estado 500
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Inicia la aplicación Flask en modo desarrollo
    app.run(host="0.0.0.0", port=5000, debug=True)
