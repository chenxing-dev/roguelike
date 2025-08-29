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
    "Forgotten": COLOR.AMBER,
    "Temple:": COLOR.AMBER,
    "Gothique": COLOR.AMBER,
    "£halice": COLOR.YELLOW,
    "Sister": COLOR.PURPLE,
    "HP": COLOR.GREEN,
    "$$": COLOR.AMBER,
    "Looter": (180, 100, 100),
    "Thug": (150, 50, 50),
    "Corrupt Cop": (50, 50, 180),
    "Heal": COLOR.GREEN,
    "Pipe Wrench": (180, 180, 220),
    "Baseball Bat": (200, 150, 100),
    "Fire Axe": (200, 50, 50),
}
