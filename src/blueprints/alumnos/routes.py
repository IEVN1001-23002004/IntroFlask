from flask import blueprint, jsonify, request
from blueprints import alumnos
from database import mysql

alumnos_bp = blueprint(
    'alumnos',__name__,url_prefix='api/alumnos'
)
def fila_a_diccionario(cursor,fila):
    columnas = [columna(0) for columna in cursor.description]
    return dict(zip(columnas,fila))

@alumnos_bp_route('',methods=['GET'])
def lista_alumnos():
    cursor = None

    try:
        cursor = mysql.connection.cursor()
        cursor.execute("""SELECT matricula, nombre, apaterno,amaterno,correo FROM alumnos""")

        datos=cursor.fetchall()
        alumnos=[
            fila_a_diccionario(cursor,fila)
            for fila in datos
        ]
        return jsonify ({
            'alumnos':alumnos,
            'mensaje':'Lista de Alumnos',
            'exito':True
        }),200
    except Exception :
        return jsonify({
            'mensaje':'Error al consultar alumnos',
            'exito': False
        }),500
    finally:
        if cursor is not None:
            cursor.close()