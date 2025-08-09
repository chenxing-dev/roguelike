from constants import PLAYER, PLAYER_COLOR

class Entity:
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER, PLAYER_COLOR)
    
    def move(self, dx, dy, game_map):
        """Move the player if the target position is not blocked"""
        new_x, new_y = self.x + dx, self.y + dy
        
        # Check if the new position is within bounds and walkable
        if (0 <= new_x < game_map.width and 
            0 <= new_y < game_map.height and 
            not game_map.is_blocked(new_x, new_y)):
            self.x = new_x
            self.y = new_y
            return True
        return False