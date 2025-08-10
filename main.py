import pygame
from engine import Engine
from entities import Player
from dungeon_gen import GameMap
from constants import MAP_WIDTH, MAP_HEIGHT, GAME_TITLE, GAME_DESCRIPTION

def main():
    # Initialize game engine
    engine = Engine()
    
    # Create game map
    game_map = GameMap(MAP_WIDTH, MAP_HEIGHT)
    
    # Sample map
    map_data = [
        "###############",
        "#....C........#",
        "#.............#",
        "#.............#",
        "#........S....#",
        "#....$........#",
        "#......@......#",
        "#..!..........#",
        "#.............#",
        "#.........>...#",
        "#.............#",
        "#...L.......T.#",
        "#.............#",
        "#.............#",
        "###############"
    ]
    game_map.load_from_string_array(map_data)
    
    # Create player at the starting position found in the map
    player = Player(*game_map.player_start)
    
    # Add starting messages
    engine.add_message(f"Welcome to {GAME_TITLE}!")
    engine.add_message(GAME_DESCRIPTION)
    engine.add_message("Find the stairs (>) to descend deeper.")
    
    # Main game loop
    running = True
    while running:
        # Handle events
        running = engine.handle_events(player, game_map)
        
        # Render everything
        engine.render(game_map, player)
        
        # Cap at 60 FPS
        engine.clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()