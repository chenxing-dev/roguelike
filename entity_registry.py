import random
from entities import (
    Actor,
    Item,
    Looter,
    Thug,
    CorruptCop,
    Heal,
    Currency,
    Weapon,
    Stairs,
)
from constants import COLOR

ENTITY_REGISTRY = {
    "L": (Looter, COLOR.RED, "Looter", 6, 2),
    "T": (Thug, COLOR.RED, "Thug", 10, 2),
    "C": (CorruptCop, COLOR.RED, "Corrupt Cop", 12, 3),
    "!": (Heal, COLOR.GREEN, "Heal", 0, 0),
    "$": (Currency, COLOR.GOLD, "Coins", 0, 0),
    ")": (Weapon, COLOR.BROWN, "Weapon", 0, 0),
    ">": (Stairs, (180, 230, 30), "Stairs", 0, 0),
}


# Generic entity classes
def create_entity(symbol, x, y):
    if symbol not in ENTITY_REGISTRY:
        return None

    cls, color, name, hp, damage = ENTITY_REGISTRY[symbol]

    if issubclass(cls, Actor):
        return cls(x, y, symbol, color, name, hp, damage)
    elif issubclass(cls, Item):
        # Special handling for item subtypes
        if cls == Currency:
            return Currency(x, y, random.randint(1, 5))
        elif cls == Weapon:
            weapons = [("Pipe Wrench", 1), ("Baseball Bat", 2), ("Fire Axe", 3)]
            name, boost = random.choice(weapons)
            return Weapon(x, y, name, boost)
        else:
            value = hp  # hp used as value for items
            return cls(x, y, symbol, color, name, value)
    else:
        return cls(x, y, symbol, color, name)
