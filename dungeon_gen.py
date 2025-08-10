import random
import numpy as np
from constants import *
from entity_registry import ENTITY_REGISTRY, create_entity


# Sample map
templates = {
        1: [
            "###############",
            "#...........$.#",
            "#.L..........S#",
            "#.............#",
            "#.............#",
            "#.............#",
            "#.....!.......#",
            "#.......@.....#",
            "#............>#",
            "#.............#",
            "#.............#",
            "#.............#",
            "#.$...........#",
            "#.............#",
            "###############"
        ],
        2: [
            "###############",
            "#.L.T.........#",
            "#.............#",
            "#.............#",
            "#.............#",
            "#.....C.......#",
            "#.....!.......#",
            "#.......@.....#",
            "#.....>.......#",
            "#.............#",
            "#.S...........#",
            "#.............#",
            "#.$...........#",
            "#.............#",
            "###############"
        ]}

class GameMap:
    def __init__(self, level=1):
        self.width = 15
        self.height = 15
        self.tiles = np.full((self.width, self.height), fill_value=FLOOR, dtype=str)
        self.player_start = (3, 3)  # default
        self.level = level
        self.entities = []  # Store entities here
    
    def generate_map(self):
        """Load map from a list of strings"""
        string_array = templates.get(self.level, templates[1])
        self.height = len(string_array)
        self.width = len(string_array[0])
        self.tiles = np.full((self.width, self.height), fill_value=FLOOR, dtype='str')
        
        self.entities = []  # Reset entities
        self.player_start = (3, 3)  # default
        
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
                    elif char in ENTITY_REGISTRY:
                        entity = create_entity(char, x, y)
                        if entity:
                            self.entities.append(entity)

        
    def is_blocked(self, x, y):
        """Check if a tile is blocked (wall)"""
        return self.tiles[x, y] == WALL