import math
from enum import Enum


class Attribute(Enum):
    STRENGTH = 1
    DEXTERITY = 2
    CONSTITUTION = 3
    INTELLIGENCE = 4
    WISDOM = 5
    CHARISMA = 6


class Attributes:
    attributes = {}

    def __init__(self, attributes: []):
        self.attributes[Attribute.STRENGTH] = attributes[0]
        self.attributes[Attribute.DEXTERITY] = attributes[1]
        self.attributes[Attribute.CONSTITUTION] = attributes[2]
        self.attributes[Attribute.INTELLIGENCE] = attributes[3]
        self.attributes[Attribute.WISDOM] = attributes[4]
        self.attributes[Attribute.CHARISMA] = attributes[5]

    def get_modifier(self, attribute: Attribute) -> int:
        return math.floor((self.attributes[attribute] - 10) / 2.0)
