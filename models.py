class Character:
    def __init__(self, id, name, skin_color, race, strength, agility, magic, knowledge):
        self.id = id
        self.name = name
        self.skin_color = skin_color
        self.race = race
        self.strength = strength
        self.agility = agility
        self.magic = magic
        self.knowledge = knowledge

    def to_dict(self):
        return self.__dict__
