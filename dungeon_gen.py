import random
import numpy as np
from constants import WALL, FLOOR, PLAYER
from entities import Scavenger, Looter, Thug, CorruptCop, FirstAid, Caps, Weapon, Stairs

class GameMap:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.tiles = np.full((width, height), fill_value=FLOOR, dtype=str)
        self.player_start = (3, 3)  # default
        self.entities = []
    
    def load_from_string_array(self, string_array):
        """Load map from a list of strings"""
        self.height = len(string_array)
        self.width = len(string_array[0])
        self.tiles = np.full((self.width, self.height), fill_value=FLOOR, dtype='str')
        
        # Convert text map to grid
        for y, row in enumerate(string_array):
            for x, char in enumerate(row):
                if x < self.width and y < self.height:
                    # Set tile type
                    if char in (WALL, FLOOR):
                        self.tiles[x, y] = char
                    else:
                        self.tiles[x, y] = FLOOR  # Entities on floor tiles
                    
                    # Place entities
                    if char == PLAYER:
                        # This is the player starting position
                        self.player_start = (x, y)
                    elif char == 'S':
                        self.entities.append(Scavenger(x, y))
                    elif char == 'L':  # Looter
                        self.entities.append(Looter(x, y))
                    elif char == 'T':  # Thug
                        self.entities.append(Thug(x, y))
                    elif char == 'C':  # Corrupt Cop
                        self.entities.append(CorruptCop(x, y))
                    elif char == '!':
                        self.entities.append(FirstAid(x, y))
                    elif char == '$':
                        self.entities.append(Caps(x, y, random.randint(1, 5)))
                    elif char == ')':
                        weapons = [
                            ("Pipe Wrench", 1),
                            ("Baseball Bat", 2),
                            ("Fire Axe", 3)
                        ]
                        name, boost = random.choice(weapons)
                        self.entities.append(Weapon(x, y, name, boost))
                    elif char == '>':
                        self.entities.append(Stairs(x, y))

        
    def is_blocked(self, x, y):
        """Check if a tile is blocked (wall)"""
        return self.tiles[x, y] == WALL