from flask import Blueprint, abort, make_response, request, Response
from app.models.planet import Planet
from app.models.moon import Moon
from ..db import db
from .route_utilities import validate_model


bp = Blueprint("moons_bp", __name__, url_prefix="/planets/<planet_id>/moons")

@bp.post("")
def create_moon_with_planet(planet_id):
    planet = validate_model(Planet, planet_id )
    request_body = request.get_json()
    request_body["planet_id"] = planet.id
    try:
        new_moon = Moon.from_dict(request_body)

    except KeyError as error:
        response = {"message": f"Invalid request: missing {error.args[0]}"}
        abort(make_response(response, 400))

    db.session.add(new_moon)
    db.session.commit()

    return new_moon.to_dict(), 201


@bp.get("")
def get_all_planet_moons(planet_id):
    planet = validate_model(Planet, planet_id)
    moons = [moon.to_dict() for moon in planet.moons]
    return moons


# @bp.get("/<planet_id>")
# def get_one_planet(planet_id):
#     planet = validate_model(Planet, planet_id)
    
#     return planet.to_dict()


# #Wave 4
# @bp.put("/<planet_id>")
# def update_one_planet(planet_id):
#     planet = validate_model(Planet, planet_id)
#     request_body = request.get_json()
    
#     planet.name = request_body["name"]
#     planet.description = request_body["description"]
#     planet.habitable = request_body["habitable"]
#     db.session.commit()

#     return Response(status=204, mimetype ="application/json")

# #Wave 4
# @bp.delete("/<planet_id>")
# def delete_one_planet(planet_id):
#     planet = validate_model(Planet, planet_id)

#     db.session.delete(planet)
#     db.session.commit()

#     return Response(status=204, mimetype ="application/json")
    