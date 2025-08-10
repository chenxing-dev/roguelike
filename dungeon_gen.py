import random
import queue
import math
import numpy as np
from constants import *
from entity_registry import ENTITY_REGISTRY, create_entity


# Sample map
templates = {
        1: [
            "###############",
            "#...........$.#",
            "#.............#",
            "#.............#",
            "#.............#",
            "#.............#",
            "#.....!.......#",
            "#.......@.S...#",
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
        
        self.fov = np.zeros((self.width, self.height), dtype=bool)
        self.explored = np.zeros((self.width, self.height), dtype=bool)
    
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
    
    def is_blocked_by_entity(self, x, y, entities):
        """Check if a position is blocked by an entity"""
        for entity in entities:
            if entity.blocks and entity.x == x and entity.y == y:
                print(f"{entity.name} is blocking the way")
                return True
        return False
    
    def compute_fov(self, player_x, player_y, radius=8):
        # Reset FOV
        self.fov.fill(False)
        
        # Simple circular FOV
        for dx in range(-radius, radius+1):
            for dy in range(-radius, radius+1):
                x = player_x + dx
                y = player_y + dy
                if 0 <= x < self.width and 0 <= y < self.height:
                    if dx*dx + dy*dy <= radius*radius:
                        self.fov[x, y] = True
                        self.explored[x, y] = True
                        
    def find_path(self, start_x, start_y, target_x, target_y, entities):
        """Simple pathfinding using Manhattan distance with obstacle avoidance"""
        # Simple movement: try to reduce distance in x or y direction
        dx = target_x - start_x
        dy = target_y - start_y
        distance = abs(dx) + abs(dy)
        
        # Possible moves (4-directional)
        moves = []
        if dx != 0:
            sign = 1 if dx > 0 else -1
            moves.append((sign, 0))
        if dy != 0:
            sign = 1 if dy > 0 else -1
            moves.append((0, sign))
        
        # Try moves in order of preference
        for move in moves:
            new_x = start_x + move[0]
            new_y = start_y + move[1]
            
            # Check if move is valid
            if (0 <= new_x < self.width and 
                0 <= new_y < self.height and
                not self.is_blocked(new_x, new_y) and
                not self.is_blocked_by_entity(new_x, new_y, entities)):
                return (new_x, new_y)
        # If no valid move, stay in place
        return (start_x, start_y)