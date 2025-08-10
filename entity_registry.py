import random
from entities import Actor, Item, Scavenger, Looter, Thug, CorruptCop, FirstAid, Caps, Weapon, Stairs

ENTITY_REGISTRY = {
    'S': (Scavenger, (180, 150, 50), "Scavenger", 8, 1),
    'L': (Looter, (180, 100, 100), "Looter", 6, 2),
    'T': (Thug, (150, 50, 50), "Thug", 10, 2),
    'C': (CorruptCop, (50, 50, 180), "Corrupt Cop", 12, 3),
    '!': (FirstAid, (255, 50, 50), "First-Aid Kit", 0, 0),
    '$': (Caps, (200, 180, 50), "Bottle Caps", 0, 0),
    ')': (Weapon, (180, 180, 220), "Weapon", 0, 0),
    '>': (Stairs, (180, 230, 30), "Stairs", 0, 0)
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
        if cls == Caps:
            return Caps(x, y, random.randint(1, 5))
        elif cls == Weapon:
            weapons = [
                ("Pipe Wrench", 1),
                ("Baseball Bat", 2),
                ("Fire Axe", 3)
            ]
            name, boost = random.choice(weapons)
            return Weapon(x, y, name, boost)
        else:
            value = hp  # hp used as value for items
            return cls(x, y, symbol, color, name, value)
    else:
        return cls(x, y, symbol, color, name)