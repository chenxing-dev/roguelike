# pylint:disable=
import pygame
from engine import Engine
from entities import Player
from dungeon_gen import GameMap
from constants import GAME_TITLE


def main():
    # Initialize game engine
    engine = Engine()

    # Create game map
    game_map = GameMap(level=1)
    game_map.generate_map()

    # Create player at the starting position found in the map
    player = Player(*game_map.player_start)

    # Add starting messages
    engine.add_message(GAME_TITLE)
    engine.add_message("")
    engine.add_message("Temple defiled.")
    engine.add_message("£halice stolen.")
    engine.add_message("Sister Evangeline:")
    engine.add_message("Descend into darkness.")
    engine.add_message("Reclaim the light.")

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
