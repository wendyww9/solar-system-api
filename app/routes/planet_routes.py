from flask import Blueprint, abort, make_response, request, Response
from app.models.planet import Planet
from ..db import db
from .route_utilities import validate_model
# from app.models.planet import planets

bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

#Wave 3
@bp.post("")
def create_planet():
    request_body = request.get_json()
    try:
        new_planet = Planet.from_dict(request_body)

    except KeyError as error:
        response = {"message": f"Invalid request: missing {error.args[0]}"}
        abort(make_response(response, 400))

    db.session.add(new_planet)
    db.session.commit()

    return new_planet.to_dict(), 201

#Wave 3 and Wave 5
@bp.get("")
def get_all_planets():
    query = db.select(Planet)
    description_param = request.args.get("description")
    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))
        
    habitable_param = request.args.get("habitable")
    if habitable_param:
        query = query.where(Planet.habitable.ilike(f"%{habitable_param}%"))
        
    query = query.order_by(Planet.id)
    planets = db.session.scalars(query)

    planets_response = []
    for planet in planets:
        planets_response.append(planet.to_dict())
    
    return planets_response

#Wave 3
@bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    
    return planet.to_dict()


#Wave 4
@bp.put("/<planet_id>")
def update_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()
    
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.habitable = request_body["habitable"]
    db.session.commit()

    return Response(status=204, mimetype ="application/json")

#Wave 4
@bp.delete("/<planet_id>")
def delete_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype ="application/json")
    

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
