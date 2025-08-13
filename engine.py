import math
import pygame
from constants import (
    GAME_TITLE,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FONT_SIZE,
    WALL,
    FLOOR,
    WALL_COLOR,
    FLOOR_COLOR,
    PLAYER,
    PLAYER_COLOR,
    GRID_WIDTH,
    GRID_HEIGHT,
    MAP_WIDTH,
    MAP_HEIGHT,
    UI_WIDTH,
    UI_HEIGHT,
    MSG_WIDTH,
    MSG_HEIGHT,
    BLACK,
    WHITE,
    PADDING_LEFT,
    PADDING_TOP,
)
from entities import Actor


class Engine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        self.clock = pygame.time.Clock()

        # Create fonts
        self.font_ui = pygame.font.Font("fonts/FT88-Gothique.ttf", FONT_SIZE)
        self.font_map = pygame.font.Font("fonts/FT88-Gothique.ttf", FONT_SIZE)

        # Calculate the size of a character
        width, height = self.font_map.size(WALL + FLOOR)
        self.char_width, self.char_height = width / 2, height

        # Create container surface
        container_width = GRID_WIDTH * self.char_width
        container_height = GRID_HEIGHT * self.char_height
        self.container = pygame.Surface(
            (container_width, container_height), pygame.SRCALPHA
        )

        # Initialize empty game messages
        self.messages = []

        self.game_state = "playing"  # "playing", "dead", "victory"

    def add_message(self, message):
        """Add a message to the log with automatic wrapping"""

        if message == "":
            self.messages.append("")
            return

        # Split long messages into chunks that fit in the message area
        max_chars = GRID_WIDTH  # Max characters per line
        words = message.split()
        lines = []
        current_line = ""

        for word in words:
            if current_line:
                # If line not empty, we need to add a space before the word
                test_line = current_line + " " + word
            else:
                # First word in line, no space needed
                test_line = word

            # Check if adding this word would exceed the line length
            if len(test_line) <= max_chars:
                current_line = test_line
            else:
                # Word doesn't fit - finish current line and start new one
                if current_line:  # Only add if not empty
                    lines.append(current_line)
                current_line = word

                # Handle words longer than max_chars
                while len(current_line) > max_chars:
                    # Split the oversized word
                    lines.append(current_line[:max_chars])
                    current_line = current_line[max_chars:]

        # Add the last line
        if current_line:
            lines.append(current_line)

        # Add all lines to message log
        for line in lines:
            self.messages.append(line)

            # Keep message log manageable
            if len(self.messages) > MSG_HEIGHT * 3:
                self.messages.pop(0)

    def render(self, game_map, player):
        """Render the game"""

        # Clear container
        self.container.fill(BLACK)

        self.render_map(game_map, player)

        # Draw UI panel
        self.render_ui_panel(player)

        # Draw message log
        self.render_messages()

        # Blit container to screen with padding
        self.screen.fill(BLACK)
        self.screen.blit(self.container, (PADDING_LEFT, PADDING_TOP))

        pygame.display.flip()

    def render_map(self, game_map, player):
        """Render the game map and entities"""

        # Draw tiles
        for x in range(game_map.width):
            for y in range(game_map.height):
                # Get the character and color for this tile
                char = game_map.tiles[x, y]
                color = WALL_COLOR if char == WALL else FLOOR_COLOR

                # Render the tile character
                text_surface = self.font_map.render(char, True, color)
                self.container.blit(
                    text_surface, (x * self.char_width, y * self.char_height)
                )

        # Draw entities

        # Create a set of positions occupied by blocking entities
        blocking_positions = set()
        for entity in game_map.entities:
            if entity.blocks and entity != player and entity.alive:
                blocking_positions.add((entity.x, entity.y))

        # Draw non-blocking entities only if not covered by blocking entities
        for entity in game_map.entities:
            if not entity.blocks and entity != player:
                if (entity.x, entity.y) not in blocking_positions:
                    text = self.font_map.render(entity.char, True, entity.color)
                    self.container.blit(
                        text, (entity.x * self.char_width, entity.y * self.char_height)
                    )

        # Second: Draw blocking entities (enemies)
        for entity in game_map.entities:
            if entity.blocks and entity != player and entity.alive:

                # Draw health indicator for enemies
                color = entity.color
                # Health indicator
                if entity.hp / entity.max_hp < 0.3:
                    color = (255, 50, 50)  # Red when critical
                elif entity.hp / entity.max_hp < 0.6:
                    color = (255, 200, 50)  # Yellow when wounded

                text = self.font_map.render(entity.char, True, color)
                self.container.blit(
                    text, (entity.x * self.char_width, entity.y * self.char_height)
                )

        # Third: Draw player (always on top)
        if player.alive:
            player_text = self.font_map.render(PLAYER, True, PLAYER_COLOR)
            self.container.blit(
                player_text, (player.x * self.char_width, player.y * self.char_height)
            )

    def render_ui_panel(self, player):
        """Render the UI panel with player stats"""
        # Draw UI panel background
        ui_x, ui_y = MAP_WIDTH * self.char_width, 0
        ui_bg = pygame.Surface(
            (UI_WIDTH * self.char_width, UI_HEIGHT * self.char_height), pygame.SRCALPHA
        )
        ui_bg.fill(BLACK)
        self.container.blit(ui_bg, (ui_x, ui_y))

        # Player stats
        stats_y = 0
        stats = [
            f"Level {player.level}",
            f"Floor {player.current_floor}",
            "",
            f"XP {player.xp}",
            f"$$ {player.caps}",
            f"HP {player.hp}/{player.max_hp}",
            "",
            f"Damage {player.damage}",
        ]

        # Draw stats with UI font
        for stat in stats:
            text = self.font_ui.render(stat, True, WHITE)
            self.container.blit(text, (ui_x + self.char_width, stats_y))
            stats_y += self.char_height

    def render_messages(self):
        """Render messages"""
        msg_x, msg_y = 0, MAP_HEIGHT * self.char_height

        # Draw message log background
        msg_bg = pygame.Surface(
            (MSG_WIDTH * self.char_width, MSG_HEIGHT * self.char_height),
            pygame.SRCALPHA,
        )
        msg_bg.fill(BLACK)
        self.container.blit(msg_bg, (msg_x, msg_y))

        # Draw messages
        for i, msg in enumerate(self.messages[-MSG_HEIGHT:]):
            # Create surface for entire message
            text = self.font_ui.render(msg, True, WHITE)
            self.container.blit(text, (0, msg_y + i * self.char_height))

    def handle_events(self, player, game_map):
        """Handle user input events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                # Always allow quitting
                if event.key == pygame.K_ESCAPE:
                    return False

                # Ignore other input if player is dead
                if not player.alive:
                    return True

                turn_passed = False
                result = ""

                # Movement controls
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    result = player.move(0, -1, game_map)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    result = player.move(0, 1, game_map)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    result = player.move(-1, 0, game_map)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    result = player.move(1, 0, game_map)
                elif event.key == pygame.K_i:
                    # Opening inventory does not pass a turn
                    self.show_inventory(player)
                    return True
                else:
                    return True

                if result is not None:  # Either moved or interacted
                    turn_passed = True
                    # Only add message if result is a string
                    if isinstance(result, str):
                        self.add_message(result)

                if turn_passed and player.alive:
                    game_map.compute_fov(player.x, player.y)
                    # Process enemy turns after player moves
                    self.handle_enemy_turns(player, game_map)

                # Remove dead entities
                game_map.entities[:] = [
                    e for e in game_map.entities if getattr(e, "alive", True)
                ]

                # Check if player died
                if not player.alive:
                    self.add_message("YOU HAVE DIED")
                    self.add_message("Game Over! Press ESC to quit.")

                # Handle stairs
                if result and isinstance(result, str) and "Descending" in result:
                    # Generate next level
                    game_map.level = player.current_floor
                    game_map.generate_map()
                    player.x, player.y = game_map.player_start

                return True

        return True

    def show_inventory(self, player):
        """Display inventory and allow item usage"""
        if not player.inventory:
            self.add_message("Your inventory is empty.")
            return

        self.add_message("Inventory:")
        for _, item in enumerate(player.inventory):
            self.add_message(item.name)

        # For now, just show the items
        # Later, let the player select one to use

    def handle_enemy_turns(self, player, game_map):
        """Process enemy turns after player moves"""
        messages = []

        for entity in game_map.entities[
            :
        ]:  # Use slice copy to avoid modification issues
            if isinstance(entity, Actor) and entity is not player and entity.alive:
                # Calculate distance to player
                distance = math.sqrt(
                    (entity.x - player.x) ** 2 + (entity.y - player.y) ** 2
                )

                if distance <= 8:  # Detection range
                    if distance <= 1:  # Check if player is adjacent
                        # Attack player
                        result = entity.attack(player)
                        messages.append(result)

                        # Check if player died
                        if not player.alive:
                            self.game_state = "dead"
                    else:
                        # Move toward player using pathfinding
                        new_x, new_y = game_map.find_path(
                            entity.x, entity.y, player.x, player.y, game_map.entities
                        )

                        # Only move if not blocked
                        if not game_map.is_blocked(new_x, new_y):
                            # Check if position is occupied
                            occupied = False
                            for other in game_map.entities:
                                if (
                                    other.blocks
                                    and other != entity
                                    and other.x == new_x
                                    and other.y == new_y
                                ):
                                    occupied = True
                                    break

                            if not occupied:
                                entity.x, entity.y = new_x, new_y

        # Add messages to log
        for msg in messages:
            self.add_message(msg)

    def move_toward(self, entity, target_x, target_y, game_map):
        # Directions: 4-way
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        # We'll try to minimize the distance to target
        best_dist = float("inf")
        best_move = (entity.x, entity.y)
        for dx, dy in directions:
            nx, ny = entity.x + dx, entity.y + dy
            if not (0 <= nx < game_map.width and 0 <= ny < game_map.height):
                continue
            if game_map.is_blocked(nx, ny):
                continue
            # Check if there's an actor in that position
            occupied = False
            for e in game_map.entities:
                if e.blocks and e.x == nx and e.y == ny and e.alive:
                    occupied = True
                    break
            if occupied:
                continue

            dist = (nx - target_x) ** 2 + (ny - target_y) ** 2
            if dist < best_dist:
                best_dist = dist
                best_move = (nx, ny)

        # Move the entity
        entity.x, entity.y = best_move
