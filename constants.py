import colors as COLOR

# Game title and description
GAME_TITLE = "Forgotten Temple: Gothique"
GAME_DESCRIPTION = ""

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 720, 720

# Grid dimensions (characters on screen)
GRID_WIDTH, GRID_HEIGHT = 32, 22

# Map dimensions
MAP_WIDTH, MAP_HEIGHT = 15, 15

# UI panel dimensions
UI_WIDTH, UI_HEIGHT = 17, 15
MSG_WIDTH, MSG_HEIGHT = 32, 7

# Padding
INNER_PADDING = 2
OUTER_PADDING = 6

# Font settings
FONT_SIZE = 32

# Symbols
WALL = "#"
FLOOR = "."
PLAYER = "S"

# Special Keywords with Colors
COLORED_WORDS = {
    "Forgotten": COLOR.RED,
    "Temple:": COLOR.RED,
    "Gothique": COLOR.RED,
    "Sister": COLOR.BLUE,
    "HP": COLOR.GREEN,
    "$$": COLOR.GOLD,
}
