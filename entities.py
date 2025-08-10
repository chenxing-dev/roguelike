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
        self.equipped_weapon = None
    
    def move(self, dx, dy, game_map):
        """Move the player if the target position is not blocked"""
        new_x, new_y = self.x + dx, self.y + dy
        
        # Check for wall collision
        if game_map.is_blocked(new_x, new_y):
            return None
        
        # Check for entity interaction at new position
        target = None
        for entity in game_map.entities:
            if entity.x == new_x and entity.y == new_y:
                target = entity
                break
            
        if target:
            if isinstance(target, Stairs):  # Check stairs first!
                return self.use_stairs(target, game_map)
            elif isinstance(target, Actor):
                return self.attack(target)
            elif isinstance(target, Item):
                # Move player first
                self.x, self.y = new_x, new_y
                return self.pick_up(target, game_map.entities)
        else:
            self.x, self.y = new_x, new_y
            return None
    
    def attack(self, target):
        # Calculate damage with equipped weapon
        damage = self.damage
        if self.equipped_weapon:
            damage += self.equipped_weapon.damage_boost
            
        result = target.take_damage(self.damage)
        return result
    
    def pick_up(self, item, entities):
        if isinstance(item, Caps):
            self.caps += item.value
            entities.remove(item)
            return f"Picked up {item.get_name()}"
        else:
            self.inventory.append(item)
            entities.remove(item)
            return f"Picked up {item.name}"
    
    def use_stairs(self, stairs, game_map):
        self.current_floor += 1
        return f"Level {self.current_floor-1} complete! Descending to level {self.current_floor}..."
    
    def use_item(self, item):
        if isinstance(item, FirstAid):
            self.hp = min(self.max_hp, self.hp + item.value)
            return f"Used first-aid kit (+{item.value} HP)"
        elif isinstance(item, Weapon):
            self.equipped_weapon = item
            return f"Equipped {item.name} (+{item.damage_boost} DMG)"
        return None
    
class Scavenger(Actor):
    def __init__(self, x, y, symbol, color, name, hp, damage):
        super().__init__(x, y, symbol, color, name, hp, damage)

class Looter(Actor):
    def __init__(self, x, y, symbol, color, name, hp, damage):
        super().__init__(x, y, symbol, color, name, hp, damage)

class Thug(Actor):
    def __init__(self, x, y, symbol, color, name, hp, damage):
        super().__init__(x, y, symbol, color, name, hp, damage)

class CorruptCop(Actor):
    def __init__(self, x, y, symbol, color, name, hp, damage):
        super().__init__(x, y, symbol, color, name, hp, damage)
        self.armor = 1  # Reduced damage taken


class Stairs(Entity):
    def __init__(self, x, y, symbol, color, name):
        super().__init__(x, y, symbol, color, name, blocks=False)        

class Item(Entity):
    def __init__(self, x, y, char, color, name, value=0):
        super().__init__(x, y, char, color, name, blocks=False)
        self.value = value

class Caps(Item):
    def __init__(self, x, y, value=1):
        super().__init__(x, y, '$', (200, 180, 50), "Bottle Caps", value)
    def get_name(self):
        if self.value == 1:
            return "1 Bottle Cap"
        return f"{self.value} Bottle Caps"
    
class FirstAid(Item):
    def __init__(self, x, y, symbol, color, name, value):
        super().__init__(x, y, symbol, color, name, value)

class Weapon(Item):
    def __init__(self, x, y, name, damage_boost):
        super().__init__(x, y, ')', (180, 180, 220), name, damage_boost)
        self.damage_boost = damage_boost
