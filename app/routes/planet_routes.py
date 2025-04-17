from flask import Blueprint
from ..models.planet import planets

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.get("")
def get_all_planets():
    planets_responce = []

    for planet in planets:
        planets_responce.append(
            dict(
                id = planet.id,
                name = planet.name,
                description = planet.description
            )
        )

    return planets_responce