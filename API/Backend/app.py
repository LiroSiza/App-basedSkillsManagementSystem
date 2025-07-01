from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
import os

# Initialize Flask app and enable CORS
app = Flask(__name__)
CORS(app)


# Configuración mínima válida para Swagger
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/swagger.json',
            "rule_filter": lambda rule: True,  # todas las rutas
            "model_filter": lambda tag: True,  # todos los modelos
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger"
}

Swagger(app, config=swagger_config)