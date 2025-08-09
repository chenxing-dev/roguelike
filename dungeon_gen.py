import numpy as np
from constants import WALL, FLOOR, PLAYER

class GameMap:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.tiles = np.full((width, height), fill_value=FLOOR, dtype=str)
        self.player_start = (3, 3)  # default
    
    def load_from_string_array(self, string_array):
        """Load map from a list of strings"""
        self.height = len(string_array)
        self.width = len(string_array[0])
        self.tiles = np.full((self.width, self.height), fill_value=FLOOR, dtype='str')
        
        # Convert text map to grid
        for y, row in enumerate(string_array):
            for x, char in enumerate(row):
                if x < self.width and y < self.height:
                    if char == PLAYER:
                        # This is the player starting position
                        self.player_start = (x, y)
                        self.tiles[x, y] = FLOOR
                    else:
                        self.tiles[x, y] = char
    
    def is_blocked(self, x, y):
        """Check if a tile is blocked (wall)"""
        return self.tiles[x, y] == WALL