# Python Snake Game 🐍

A classic 2D Snake game implementation that runs entirely in the terminal using Python's curses library.

## Description

This is a terminal-based implementation of the classic Snake game. Control the snake to eat food, grow longer, and achieve the highest score possible without hitting the walls or yourself!

## Features

### Core Features
- **Terminal-based graphics** using curses library
- **Smooth snake movement** with arrow key controls
- **Score tracking** with high score persistence during session
- **Collision detection** for walls and self
- **Random food generation**
- **Game over and restart functionality**
- **Clean, modular code** with proper documentation

### Advanced Features ✨
- **Progressive Level System** - Difficulty increases as you score more points
- **Dynamic Obstacles** - Walls appear at higher levels to increase challenge
- **Multiple Snake Skins** - Choose from 4 different visual styles (classic, blocks, arrows, dots)
- **Persistent Leaderboard** - Top 10 scores saved across sessions with timestamps
- **Pause/Resume** - Pause the game anytime with 'P' key
- **Speed Progression** - Game speed increases with each level

## Requirements

- Python 3.8.1 or higher
- Unix/Linux/macOS (with curses support built-in)
- Windows (requires `windows-curses` package)

## CI/CD Pipeline

This project includes a comprehensive CI/CD pipeline using GitHub Actions:

- ✅ Automated linting with flake8
- ✅ Cross-platform testing (Ubuntu, Windows, macOS)
- ✅ Multi-version Python testing (3.8-3.12)
- ✅ Package building with Poetry
- ✅ Publishing to GitHub Packages
- ✅ Documentation deployment to GitHub Pages

**For detailed CI/CD documentation**, see [CI_CD.md](CI_CD.md)

## Quick Start

**Want to get started immediately?** Check out the [QUICKSTART.md](QUICKSTART.md) guide for a streamlined setup process!

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

**Option A: Using pip (Simple)**
```bash
pip install -r requirements.txt
```

**Option B: Using Poetry (Recommended for development)**
```bash
pip install poetry
poetry install
```

**Note:** On Unix/Linux/macOS, no external dependencies are needed as curses is part of the standard library. On Windows, the `windows-curses` package will be installed automatically.

## Usage

### Running the Game

**Using Python directly:**
```bash
python snake_game.py
```

**Using Poetry:**
```bash
poetry run snake-game
```

**Or make it executable and run directly (Unix/Linux/macOS):**
```bash
chmod +x snake_game.py
./snake_game.py
```

### Game Controls

- **Arrow Keys**: Control snake direction (Up, Down, Left, Right)
- **P**: Pause/Resume the game
- **S**: Change snake skin (cycle through available skins)
- **L**: View leaderboard (also available at game over)
- **R**: Restart the game
- **Q**: Quit the game

**For detailed gameplay instructions and strategies, see [GAMEPLAY.md](GAMEPLAY.md)**

### Game Rules

1. The snake starts with a length of 3 segments at Level 1
2. Use arrow keys to move the snake
3. Eat the food (`*`) to grow longer and increase your score
4. Each food eaten gives you 10 points
5. Every 50 points, you advance to the next level
6. Higher levels increase game speed and add obstacles (#)
7. Avoid hitting the walls, obstacles, or your own body
8. The game ends when you collide with a wall, obstacle, or yourself
9. Your top 10 scores are saved to the leaderboard
10. Try to achieve the highest score!

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
