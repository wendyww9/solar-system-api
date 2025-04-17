class Planet:
    def __init__(self, id, name, description, species=None):
        self.id = id
        self.name = name
        self.description = description
        self.species = species

planets = [
    Planet(1, "Tatooine", "A desert planet with twin suns, home of Anakin and Luke Skywalker."),
    Planet(2, "Naboo", "A lush, green planet known for its beautiful landscapes and Queen Amidala."),
    Planet(3, "Alderaan", "A peaceful planet destroyed by the Death Star."),
    Planet(4, "Endor", "Forest moon inhabited by Ewoks, key site of the Empire's downfall."),
    Planet(5, "Mustafar", "A volcanic planet where Obi-Wan and Anakin had their legendary duel."),
    Planet(6, "Jakku", "A junkyard desert planet where Rey begins her journey.")
]