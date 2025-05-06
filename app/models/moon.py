from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from sqlalchemy import ForeignKey
from typing import Optional

class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    size: Mapped[str]
    description: Mapped[str]
    orbit_period: Mapped[str]
    planet_id: Mapped[Optional[int]] = mapped_column(ForeignKey("planet.id"))
    planet: Mapped[Optional["Planet"]] = relationship(back_populates="moons")

    def to_dict(self):
        moon_as_dict = {}
        moon_as_dict["id"] = self.id
        moon_as_dict["size"] = self.size
        moon_as_dict["description"] = self.description
        moon_as_dict["orbit_period"] = self.orbit_period
        moon_as_dict["planet"] = self.planet.name if self.planet_id else None

        return moon_as_dict  
    
    @classmethod
    def from_dict(cls, moon_data):
        planet_id = moon_data.get("planet_id")
        
        new_moon = Moon(size=moon_data["size"],
            description=moon_data["description"],
            orbit_period=moon_data["orbit_period"],
            planet_id=planet_id)
        return new_moon  
