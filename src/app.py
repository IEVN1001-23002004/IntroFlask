from flask import Flask, jsonify, request,blueprint
from flask_cors import CORS
from flask_mysqldb import MySQL
from config import config
from blueprints.alumnos import alumnos_bp
from blueprints.maestros import alumnos_bp

app = Flask(__name__)
app.register_blueprint(alumnos_bp)
app.register_blueprint(maestros_bp)

CORS(app)

con = MySQL(app)


def pagina_no_encontrada(error):
    return "<h1> Pagina no Encontrada</h1>"

if __name__ == "__main__":
    app.config.from_object(config["development"])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(host="0.0.0.0", port=5000) 