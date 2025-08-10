from constants import PLAYER, PLAYER_COLOR

class Entity:
    def __init__(self, x, y, char, color, name, blocks=False):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks = blocks

class Actor(Entity):
    def __init__(self, x, y, char, color, name, hp, damage):
        super().__init__(x, y, char, color, name, blocks=True)
        self.hp = hp
        self.max_hp = hp
        self.damage = damage
        self.alive = True
        self.armor = 0

    def take_damage(self, amount):
        # Apply armor reduction
        actual_damage = max(1, amount - self.armor)
        
        self.hp -= actual_damage
        if self.hp <= 0:
            self.alive = False
            return f"{self.name} dies!"
        return f"{self.name} takes {actual_damage} damage!"

class Player(Actor):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER, PLAYER_COLOR, "Survivor", hp=10, damage=1)
        self.inventory = []
        self.caps = 0
        self.level = 1
        self.xp = 0
        self.current_floor = 1
    
    def move(self, dx, dy, game_map):
        """Move the player if the target position is not blocked"""
        new_x, new_y = self.x + dx, self.y + dy
        
        # Check for wall collision
        if game_map.is_blocked(new_x, new_y):
            return None
        
        # Check for entity interaction
        target = None
        for entity in game_map.entities:
            if entity.x == new_x and entity.y == new_y:
                target = entity
                break
            
        if target:
            if isinstance(target, Actor):
                return self.attack(target)
            elif isinstance(target, Item):
                return self.pick_up(target, game_map)
            elif isinstance(target, Stairs):
                print("target is stairs")
                return self.use_stairs(target, game_map)
        else:
            self.x, self.y = new_x, new_y
            return None
    
    def attack(self, target):
        result = target.take_damage(self.damage)
        return result
    
    def pick_up(self, item, game_map):
        if isinstance(item, Caps):
            self.caps += item.value
            game_map.entities.remove(item)
            return f"Picked up {item.value} bottle caps"
        elif isinstance(item, FirstAid):
            self.hp = min(self.max_hp, self.hp + item.value)
            game_map.entities.remove(item)
            return f"Used first-aid kit (+{item.value} HP)"
        elif isinstance(item, Weapon):
            self.damage += item.damage_boost
            game_map.entities.remove(item)
            return f"Equipped {item.name} (+{item.damage_boost} DMG)"
        return ""
    
    def use_stairs(self, stairs, game_map):
        # Placeholder for level transition
        return "Descending to the next level..."
    
    
class Scavenger(Actor):
    def __init__(self, x, y):
        super().__init__(x, y, 'S', (180, 100, 50), "Scavenger", 10, 2)

class Looter(Actor):
    def __init__(self, x, y):
        super().__init__(x, y, 'L', (180, 100, 100), "Looter", 8, 3)

class Thug(Actor):
    def __init__(self, x, y):
        super().__init__(x, y, 'T', (150, 50, 50), "Thug", 12, 4)

class CorruptCop(Actor):
    def __init__(self, x, y):
        super().__init__(x, y, 'C', (50, 50, 180), "Corrupt Cop", 15, 5)
        self.armor = 1  # Reduced damage taken
        
class Item(Entity):
    def __init__(self, x, y, char, color, name, value=0):
        super().__init__(x, y, char, color, name, blocks=False)
        self.value = value

class Caps(Item):
    def __init__(self, x, y, value=1):
        super().__init__(x, y, '$', (200, 180, 50), "Bottle Caps", value)

class FirstAid(Item):
    def __init__(self, x, y):
        super().__init__(x, y, '!', (255, 50, 50), "First-Aid Kit", 5)

class Weapon(Item):
    def __init__(self, x, y, name, damage_boost):
        super().__init__(x, y, ')', (180, 180, 220), name, damage_boost)
        self.damage_boost = damage_boost

class Stairs(Item):
    def __init__(self, x, y):
        super().__init__(x, y, '>', (180, 230, 30), "Stairs", 0)