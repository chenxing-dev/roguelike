# Hildegard's Mess - 炼金学徒日常

![Game Screenshot](screenshots/gameplay.png) <!-- 稍后添加 -->

A text-based roguelike game with gothic pixel typography, where you play as Lina, an apprentice tasked with cleaning up your mentor's magically disordered laboratory. Explore the chaotic lab, recover lost formulas, pacify unstable magical creations, and restore order through alchemy and clever problem-solving. Built with PyGame.

## Features

*   **Pure Text Rendering:** World built entirely from characters and symbols
*   **Gothic Pixel Aesthetic:** FT88 Gothique font creates an illuminated manuscript feel
*   **Roguelike Elements:** Each playthrough features a procedurally generated map layout with different challenges
*   **Alchemy System:** Collect ingredients and discover formulas to create useful potions and items
*   **Unique Pacification Mechanics**: Use brewed concoctions to calm magical creatures instead of combat

## Controls

*   **Movement:** `WASD` or `Arrow Keys`
*   **Interact/Confirm:** `E` or `Spacebar`
*   **Brew at Station**: B (when near an alchemy station)
*   **Inventory**: I
*   **Quit**: Q or ESC

## Installation

### Requirements

*   Python 3.8+
*   PyGame 2.0+ (`pip install pygame`)
*   NumPy

### Using Virtual Environment (Recommended)

1.  Clone the repository:
    ```bash
    git clone https://github.com/chenxing-dev/roguelike.git
    cd roguelike
    ```
2.  Create and activate virtual environment:
    ```bash
    # Create virtual environment
    python -m venv venv

    # Activate (Linux/macOS)
    source venv/bin/activate

    # Activate (Windows)
    venv/Scripts/activate
    ```

3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4.  Run the game:
    ```bash
    python main.py
    ```

### Building Executable

To create a standalone executable:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --add-data "assets:assets" src/main.py
```

## Project Structure

```
.
├── assets/
│   └── fonts/
│       └── FT88_Gothique.ttf    # Game font
├── src/
│   ├── main.py                  # Game entry point
│   ├── game.py                  # Main game loop
│   ├── player.py                # Player class
│   ├── world.py                 # Map generation
│   ├── entities/
│   │   ├── entity.py            # Entity base class
│   │   ├── enemy.py             # Enemy entities
│   │   └── item.py              # Item system
│   ├── systems/
│   │   ├── crafting.py          # Crafting system
│   │   └── inventory.py         # Inventory management
│   └── ui/
│       ├── hud.py               # Heads-up display
│       └── text_renderer.py     # Text renderer
├── requirements.txt             # Python dependencies
├── LICENSE                      # Code license
├── README.md                    # Project documentation
└── TODO.md                      # Development tasks
```

## 贡献

本项目为个人开发项目，暂不接受外部贡献。

## 许可证

Code is licensed under [MIT License](LICENSE).

This game uses the FT88 Gothique font from the [Degheest](https://velvetyne.fr/fonts/degheest/) project, available under the [SIL OPEN FONT LICENSE](License SIL OFL.txt).

---

*《炼金学徒日常》是正在开发中的游戏，所有功能可能会有变动。*
