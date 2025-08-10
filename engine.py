import pygame
from constants import *
from entities import Actor

class Engine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        self.clock = pygame.time.Clock()
        
        # Create fonts
        try:
            self.font_ui = pygame.font.Font("fonts/FT88-Regular.ttf", FONT_SIZE)
            self.font_map = pygame.font.Font("fonts/FT88-Gothique.ttf", FONT_SIZE)
        except:
            self.font_ui = pygame.font.SysFont("monospace", FONT_SIZE)
            self.font_map = self.font_ui 
            
        # Calculate the size of a character
        width, height = self.font_map.size(WALL + FLOOR)
        self.char_width, self.char_height = width/2, height
        
        # Create container surface
        container_width = GRID_WIDTH * self.char_width
        container_height = GRID_HEIGHT * self.char_height
        self.container = pygame.Surface((container_width, container_height), pygame.SRCALPHA)
        
        # Initialize empty game messages
        self.messages = []
        
    def add_message(self, message):
        """Add a message to the log with automatic wrapping"""
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
        self.render_ui_panel()
        
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
                self.container.blit(text_surface, (x * self.char_width, y * self.char_height))
        
        # Draw entities
        for entity in game_map.entities:
            if isinstance(entity, Actor):
                color = entity.color
                # Health indicator
                if entity.hp / entity.max_hp < 0.3:
                    color = (255, 50, 50)  # Red when critical
                elif entity.hp / entity.max_hp < 0.6:
                    color = (255, 200, 50)  # Yellow when wounded
            else:
                color = entity.color
                
            text = self.font_map.render(entity.char, True, color)
            self.container.blit(text, 
                              (entity.x * self.char_width, 
                               entity.y * self.char_height))
        
        # Draw player
        player_text = self.font_map.render(player.char, True, player.color)
        self.container.blit(player_text, (player.x * self.char_width, player.y * self.char_height))
    
    
    def render_ui_panel(self):
        """Render UI Panel"""
        ui_x, ui_y = MAP_WIDTH * self.char_width, 0
        
        # Draw UI panel background
        ui_bg = pygame.Surface((UI_WIDTH * self.char_width, UI_HEIGHT * self.char_height), pygame.SRCALPHA)
        ui_bg.fill(UI_BG_COLOR)
        self.container.blit(ui_bg, (ui_x, ui_y))
        
        # Draw UI text
        ui_text = self.font_ui.render("Player Stats", True, WHITE)
        self.container.blit(ui_text, (ui_x, 0))
    
    
    def render_messages(self):
        """Render messages"""
        msg_x, msg_y = 0, MAP_HEIGHT * self.char_height
        msg_width, msg_height = MSG_WIDTH * self.char_width, MSG_HEIGHT * self.char_height
        
        # Draw message log background
        msg_bg = pygame.Surface((MSG_WIDTH * self.char_width, MSG_HEIGHT * self.char_height), pygame.SRCALPHA)
        msg_bg.fill(MSG_BG_COLOR)
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
                elif event.key == pygame.K_ESCAPE:
                    return False
                
                if result:
                    self.add_message(result)
                    
                # Remove dead entities
                game_map.entities[:] = [e for e in game_map.entities if getattr(e, 'alive', True)]
                
                # Handle stairs
                if result and "Descending" in result:
                    # Placeholder for level transition
                    self.add_message("Level complete! Descending...")
                    # Reset level would go here
                
                return True
        
        return True