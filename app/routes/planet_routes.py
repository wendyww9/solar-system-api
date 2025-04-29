from flask import Blueprint, abort, make_response, request, Response
from app.models.planet import Planet
from ..db import db
# from app.models.planet import planets

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

#Wave 3
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

#Wave 3
@planets_bp.get("")
def get_all_planets():
    query = db.select(Planet)
    description_param = request.args.get("description")
    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))
        
    habitable_param = request.args.get('habitable')
    if habitable_param:
        query = query.where(Planet.habitable.ilike(f"%{habitable_param}%"))
        
    query = query.order_by(Planet.id)
    query = db.select(Planet)

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

#Wave 3
@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    
    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "habitable": planet.habitable
    }

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        response = {"message": f"planet with {planet_id} invalid"}
        abort(make_response(response, 400))
    
    query = db.select(Planet).where(Planet.id == planet_id)
    planet = db.session.scalar(query)

    if not planet:
        response = {"message": f"planet with {planet_id} does not exist"}
        abort(make_response(response, 404))

    return planet

#Wave 4
@planets_bp.put("/<planet_id>")
def update_one_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.json
    
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.habitable = request_body["habitable"]
    db.session.commit()

    return Response(status=204, mimetype ="application/json")

#Wave 4
@planets_bp.delete("/<planet_id>")
def delete_one_planet(planet_id):
    planet = validate_planet(planet_id)

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
