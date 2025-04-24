from flask import Blueprint, abort, make_response, request
from app.models.planet import Planet
from ..db import db
# from app.models.planet import planets

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    habitable = request_body["habitable"]

    new_planet = Planet(name=name, description=description, habitable=habitable)
    db.session.add(new_planet)
    db.session.commit()

    response = {
        "id": new_planet.id,
        "name": new_planet.name,
        "description": new_planet.description,
        "habitable": new_planet.habitable
    }
    return response, 201

@planets_bp.get("")
def get_all_planets():
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.scalars(query)
    planets_response = []
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "habitable": planet.habitable
            }
        )
    
    return planets_response

# @planets_bp.get("")
# def get_all_planets():
#     planets_response = []

#     for planet in planets:
#         planets_response.append(
#             dict(
#                 id = planet.id,
#                 name = planet.name,
#                 description = planet.description,
#                 habitable = planet.habitable
#             )
#         )

#     return planets_responce

# @planets_bp.get("/<id>")
# def get_one_planet(id):
#     planet = validate_planet(id)
#     return {
#         "id": planet.id,
#         "name": planet.name,
#         "description": planet.description,
#         "species": planet.species
#     }

# def validate_planet(id):
#     try:
#         id = int(id)
#     except:
#         invalid_msg = {"message": f"planet id ({id}) invalid"}
#         abort(make_response(invalid_msg, 400))

#     for planet in planets:
#         if planet.id == id:
#             return planet
    
#     response = {"message": f"planet {id} not found"}
#     abort(make_response(response, 404))
