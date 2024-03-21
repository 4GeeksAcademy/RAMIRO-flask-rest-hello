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
from models import db, Personas
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

@app.route('/personas', methods=['GET'])
def get_all_personas():
    all_personas = Personas.query.all()
    map_personas = list(map(lambda item: item.serialize(), all_personas ))

    if all_personas == []:
        return {"msg":"No hay personas creadas"}

    response_body = {
        "msg": "Hello, this is your GET /user response "
        "Personas" : map_personas
    }

    return jsonify(response_body), 200

# @app.route('/planetas', methods=['GET'])
# def get_all_usuarios():
#     all_planetas = Planetas.query.all()
#     print(all_planetas)

#     response_body = {
#         "msg": "Hello, this is your GET /user response "
#         # "Planetas" : all_planetas.serialize()
#     }

#     return jsonify(response_body), 200


# @app.route('/vehiculos', methods=['GET'])
# def get_all_usuarios():
#     all_vehiculos = Vehiculos.query.all()
#     print(all_vehiculos)

#     response_body = {
#         "msg": "Hello, this is your GET /user response "
#         # "Vehiculos" : Vehiculos.serialize()
#     }

#     return jsonify(response_body), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
