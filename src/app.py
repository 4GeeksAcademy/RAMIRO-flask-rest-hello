"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Personas, Planetas, Vehiculos, Usuarios, Favoritos
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


# Todos los metodos get para obtener todos los vehiculos, personajes y planetas


@app.route('/personas', methods=['GET'])
def get_all_personas():
    all_personas = Personas.query.all()
    map_personas = list(map(lambda item: item.serialize(), all_personas ))

    if all_personas == []:
        return {"msg":"No hay personas creadas"}, 404

    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "Personas" : map_personas
    }

    return jsonify(response_body), 200

@app.route('/planetas', methods=['GET'])
def get_all_planetas():
    all_planetas = Planetas.query.all()
    map_planetas = list(map(lambda item: item.serialize(), all_planetas ))
    print(all_planetas)

    if all_planetas == []:
        return {"msg":"No hay planetas creados"}, 404

    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "Planetas" : map_planetas
    }

    return jsonify(response_body), 200


@app.route('/vehiculos', methods=['GET'])
def get_all_vehiculos():
    all_vehiculos = Vehiculos.query.all()
    map_vehiculos = list(map(lambda item: item.serialize(), all_vehiculos ))
    print(all_vehiculos)

    if all_vehiculos == []:
        return {"msg":"No hay vehiculos creados"}, 404

    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "Vehiculos" : map_vehiculos
    }

    return jsonify(response_body), 200






# Metodos get para obtener solo un personaje o vehiculo o planeta en especifico


@app.route('/personas/<int:personas_id>', methods=['GET'])
def get_one_personas(personas_id):
    one_personas = Personas.query.filter_by(id = personas_id).first()

    if one_personas == None:
        return {"msg":"No existen personas creadas con ese ID"}, 404

    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "Personas" : one_personas.serialize()
    }

    return jsonify(response_body), 200

@app.route('/planetas/<int:planetas_id>', methods=['GET'])
def get_one_planetas(planetas_id):
    one_planetas = Planetas.query.filter_by(id = planetas_id).first()

    if one_planetas == None:
        return {"msg":"No existen planetas creados con ese ID"}, 404

    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "Planetas" : one_planetas.serialize()
    }

    return jsonify(response_body), 200


@app.route('/vehiculos/<int:vehiculos_id>', methods=['GET'])
def get_one_vehiculos(vehiculos_id):
    one_vehiculos = Vehiculos.query.filter_by(id = vehiculos_id).first()

    if one_vehiculos == None:
        return {"msg":"No existen vehiculos creados con ese ID"}, 404

    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "Vehiculos" : one_vehiculos.serialize()
    }

    return jsonify(response_body), 200





# Metodo para obtener todos los usuarios

@app.route('/usuarios', methods=['GET'])
def get_all_usuarios():
    all_usuarios = Usuarios.query.all()
    map_usuarios = list(map(lambda item: item.serialize(), all_usuarios ))
    print(all_usuarios)

    if all_usuarios == []:
        return {"msg":"No hay usuarios creados"}, 404

    response_body = {
        "msg": "Hello, this is your GET /user response",
        "Usuarios" : map_usuarios
    }

    return jsonify(response_body), 200





# Metodo para obtener los favoritos de un usuario
@app.route('/usuarios/favoritos/<int:usuario_id_fav>', methods=['GET'])
def get_all_favoritos_one_usuario(usuario_id_fav):
    all_favoritos_usuario = Favoritos.query.filter_by(usuario_id = usuario_id_fav).all()
    map_favoritos_usuario = list(map(lambda item: item.serialize(), all_favoritos_usuario ))

    if all_favoritos_usuario == []:
        return {"msg":"El usuario no tiene favoritos"}, 404

    response_body = {
        "msg": "Hello, this is your GET /user response",
        "Usuarios" : map_favoritos_usuario
    }

    return jsonify(response_body), 200



# Metodo para añadar un favorito
# {
#     "personas_id": 1,
#     "planetas_id": null,
#     "vehiculos_id": null,
#     "usuario_id": 2
# }

@app.route('/usuarios/favoritos', methods=['POST'])
def post_one_favorito():
    data = request.json
    print(data)
    info= Favoritos(personas_id=data["personas_id"],planetas_id=data["planetas_id"],vehiculos_id=data["vehiculos_id"],usuario_id=data["usuario_id"])
    db.session.add(info)
    db.session.commit()


    response_body = {
        "msg": "Se guardo en favoritos exitosamente",
        "Usuarios" : data
    }

    return jsonify(response_body), 200



# Metodo para eliminar un Favorito
# {
#     "favorito_id":1
# }

@app.route('/usuarios/favoritos', methods=['DELETE'])
def delete_one_favorito():
    data = request.json
    
    user_id = data["favorito_id"]
    user_to_delete = Favoritos.query.get(user_id)
    print(user_to_delete)

    if user_to_delete:
        db.session.delete(user_to_delete)
        db.session.commit()
        print(f"User with ID {user_id} deleted successfully.")

        response_body = {
        "msg": "Se Elimino en favoritos exitosamente",
        "Usuarios" : data
        }


        return jsonify(response_body), 200


    else:
        return(f"User with ID {user_id} not found."), 404


    



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
