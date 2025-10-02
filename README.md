# Python Snake Game 🐍

A classic 2D Snake game implementation that runs entirely in the terminal using Python's curses library.

## Description

This is a terminal-based implementation of the classic Snake game. Control the snake to eat food, grow longer, and achieve the highest score possible without hitting the walls or yourself!

## Features

- **Terminal-based graphics** using curses library
- **Smooth snake movement** with arrow key controls
- **Score tracking** with high score persistence during session
- **Collision detection** for walls and self
- **Random food generation**
- **Game over and restart functionality**
- **Clean, modular code** with proper documentation

## Requirements

- Python 3.6 or higher
- Unix/Linux/macOS (with curses support built-in)
- Windows (requires `windows-curses` package)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/thiyagij/python_snake_game.git
cd python_snake_game
```

### 2. Create a virtual environment (recommended)

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

**On Unix/Linux/macOS:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

**Note:** On Unix/Linux/macOS, no external dependencies are needed as curses is part of the standard library. On Windows, the `windows-curses` package will be installed automatically.

## Usage

### Running the Game

```bash
python snake_game.py
```

Or make it executable and run directly (Unix/Linux/macOS):

```bash
chmod +x snake_game.py
./snake_game.py
```

### Game Controls

- **Arrow Keys**: Control snake direction (Up, Down, Left, Right)
- **R**: Restart the game
- **Q**: Quit the game

### Game Rules

1. The snake starts with a length of 3 segments
2. Use arrow keys to move the snake
3. Eat the food (`*`) to grow longer and increase your score
4. Each food eaten gives you 10 points
5. Avoid hitting the walls or your own body
6. The game ends when you collide with a wall or yourself
7. Try to achieve the highest score!

## Project Structure

```
python_snake_game/
├── snake_game.py       # Main game file with all game logic
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── .gitignore         # Git ignore rules
└── venv/              # Virtual environment (created after setup)
```

## Code Structure

The game is organized into a single, well-documented class:

- **SnakeGame**: Main game class that handles:
  - Game initialization and setup
  - Snake movement and collision detection
  - Food generation
  - Rendering (drawing the snake, food, borders, score)
  - Input handling
  - Game state management
  - Game over logic

## Development

### Setting up the development environment

1. Follow the installation steps above
2. Make sure you have activated the virtual environment
3. The game uses only Python standard library modules (except `windows-curses` on Windows)

### Code Quality

The code follows Python best practices:
- PEP 8 style guidelines
- Comprehensive docstrings
- Clear variable and function names
- Modular design with single responsibility principle

## Troubleshooting

### Terminal size issues

If the game doesn't display correctly, ensure your terminal window is large enough (recommended: at least 80x24 characters).

### Windows issues

If you encounter issues on Windows, make sure you have installed the `windows-curses` package:

```bash
pip install windows-curses
```

### Curses not available

If you get a "No module named '_curses'" error on Unix/Linux:

```bash
# On Ubuntu/Debian
sudo apt-get install python3-dev

# On Fedora/RHEL
sudo yum install python3-devel

# On macOS
# curses should be included by default
```

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## License

This project is open source and available for educational purposes.

## Author

Thiyagi J

## Acknowledgments

- Inspired by the classic Snake game
- Built with Python's curses library for terminal graphics

---

Enjoy playing the Snake Game! 🐍🎮
