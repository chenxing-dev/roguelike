# Abandoned City Roguelike

![Game Screenshot](screenshot.png)

A minimalistic text-based roguelike game set in a procedurally generated abandoned city. Descend through 6 levels of decaying urban infrastructure, battling enemies and collecting gear to survive the depths of the forgotten city.

## Features

- Procedurally generated dungeon levels
- 6 distinct dungeon levels to explore
- Character progression system with stats and leveling
- Diverse enemy types with unique behaviors
- Equipment system with weapons and armor
- Fog of war and exploration mechanics
- Permadeath system
- Clean UI with health bars and status information

## Installation

### Prerequisites
- Python 3.8+
- Pygame
- Numpy
- Noise

### Setup
1. Clone the repository:
```bash
git clone https://github.com/chenxing-dev/abandoned-city-roguelike.git
cd abandoned-city-roguelike
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the game:
```bash
python main.py
```

## Controls
- **Movement**: Arrow Keys or WASD
- **Interact**: Walk into items/stairs
- **Quit**: ESC

## Game Mechanics

### Character Stats
- **LVL**: Player level (increases through XP)
- **HP**: Health points (0 = death)
- **ST**: Strength (affects damage)
- **DX**: Dexterity (affects dodge chance)
- **XP**: Experience points
- **DM**: Damage dealt
- **EV**: Evasion chance
- **AC**: Armor class (damage reduction)

### Entities
- **Player**: `@` - You!
- **Stairs**: `>` - Descend to next level
- **Radroach**: `R` - Weak but numerous
- **Scavenger**: `S` - Medium strength
- **Ghoul**: `G` - Strong melee fighter

### Items
- **First-Aid Kits**: `!` - Restore HP
- **Caps**: `$` - Score points
- **Weapons**: `)` - Increase damage
- **Armor**: `[` - Increase AC

## Project Structure

```plaintext
abandoned-city-roguelike/
├── main.py             # Game entry point
├── engine.py           # Main game loop and rendering
├── entities.py         # Entity classes (Player, Monster, Item)
├── dungeon_gen.py      # Procedural level generation
├── constants.py        # Game constants and configuration
├── requirements.txt    # Dependencies
├── README.md           # This file
└── fonts               # Game font
```

## Development

### Modules Overview

#### `main.py`
The entry point of the application. Initializes and runs the game.

#### `engine.py`
Contains the `Game` class which handles:
- Main game loop
- Input processing
- Rendering and UI
- Game state management

#### `entities.py`
Defines all game entities:
- `Entity`: Base class for all game objects
- `Player`: Player character with stats and inventory
- `Monster`: Enemy entities with AI behavior
- `Item`: Collectible objects with various effects

#### `dungeon_gen.py`
Handles procedural level generation:
- `GameMap` class for managing level state
- Perlin noise-based map generation
- Fog of war implementation
- Entity placement algorithms

#### `constants.py`
Contains all game constants:
- Screen dimensions and grid sizes
- Color definitions
- Game configuration parameters

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Acknowledgments

- Inspired by classic roguelike games
- Uses Pygame for graphics and input handling
- [Degheest](https://velvetyne.fr/fonts/degheest/) by Ange Degheest, Camille Depalle, Eugénie Bidaut, Luna Delabre, Mandy Elbé, May Jolivet, Oriane Charvieux, Benjamin Gomez, Justine Herbel. Distributed by velvetyne.fr.
