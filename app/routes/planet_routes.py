from flask import Blueprint, abort, make_response
from app.models.planet import planets

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.get("")
def get_all_planets():
    planets_response = []

    for planet in planets:
        planets_response.append(
            dict(
                id = planet.id,
                name = planet.name,
                description = planet.description,
                habitable = planet.habitable
            )
        )

    return planets_response

@planets_bp.get("/<id>")
def get_one_planet(id):
    planet = validate_planet(id)

    return dict(
        id = planet.id,
        name = planet.name,
        description = planet.description,
        habitable = planet.habitable
    )

def validate_planet(id):
    try:
        id = int(id)
    except:
        invalid = {"message": f"Planet id {id} is invalid"}
        abort(make_response(invalid, 400))

    for planet in planets:
        if planet.id == id:
            return planet
    not_found = {"message": f"Planet with id {id} not found"}
    abort(make_response(not_found, 404))