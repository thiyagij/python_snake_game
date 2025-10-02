# Python Snake Game 🐍

A classic 2D Snake game implementation that runs entirely in the terminal using Python's curses library.

## Description

This is a terminal-based implementation of the classic Snake game. Control the snake to eat food, grow longer, and achieve the highest score possible without hitting the walls or yourself!

## 🎮 Game Preview

### Starting Screen
```
┌────────────────────────────────────────────────────────────┐
│                      SNAKE GAME                            │
│        Arrow Keys: Move | P: Pause | R: Restart | Q: Quit  │
├────────────────────────────────────────────────────────────┤
│                                                            │
│                                                            │
│                         Ooo                                │
│                                                            │
│                              *                             │
│                                                            │
│                                                            │
└────────────────────────────────────────────────────────────┘
Score: 0                                      High Score: 0
```

### Mid-Game Action
```
┌────────────────────────────────────────────────────────────┐
│                      SNAKE GAME                            │
│        Arrow Keys: Move | P: Pause | R: Restart | Q: Quit  │
├────────────────────────────────────────────────────────────┤
│                                                            │
│              Oooooo                                        │
│              oooooo                                        │
│                 ooo                                        │
│     *                                                      │
│                                                            │
│                                                            │
└────────────────────────────────────────────────────────────┘
Score: 70                                    High Score: 150
```

### 📹 Demo Video

Coming soon! Watch gameplay footage and tips.

### 🖼️ Screenshots & GIFs

More gameplay screenshots and animated GIFs will be added here soon!

## Features

- **Terminal-based graphics** using curses library
- **Smooth snake movement** with arrow key controls
- **Score tracking** with persistent high score saved to disk
- **Pause/Resume functionality** for interruption-free gaming
- **Collision detection** for walls and self
- **Random food generation**
- **Game over and restart functionality**
- **Clean, modular code** with proper documentation

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

## 🎉 What's New?

This project has been enhanced with new features and improvements! Check out [ENHANCEMENTS.md](ENHANCEMENTS.md) for a complete summary of:
- Pause/Resume functionality
- Persistent high scores
- Modular architecture
- Enhanced documentation
- Complete CI/CD pipeline

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
- **R**: Restart the game
- **Q**: Quit the game

**For detailed gameplay instructions and strategies, see [GAMEPLAY.md](GAMEPLAY.md)**

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
├── snake_game.py           # Main game (monolithic version)
├── snake_game_modular.py   # Modular version
├── game_config.py          # Game configuration
├── score_manager.py        # High score persistence
├── game_renderer.py        # Display rendering
├── test_game.py            # Test suite
├── requirements.txt        # Python dependencies
├── setup.sh                # Unix/Linux/macOS setup script
├── setup.bat               # Windows setup script
├── pyproject.toml          # Poetry configuration
├── README.md               # This file
├── GAMEPLAY.md             # Detailed gameplay guide
├── QUICKSTART.md           # Quick start guide
├── ARCHITECTURE.md         # Architecture documentation
├── CI_CD.md                # CI/CD documentation
└── .github/
    └── workflows/
        └── ci-cd.yml       # CI/CD pipeline
```

## Code Structure

The game is available in two versions:

**Monolithic Version** (`snake_game.py`):
- Single-file implementation
- All logic in one well-documented class
- Perfect for learning and quick understanding

**Modular Version** (`snake_game_modular.py`):
- Refactored into separate modules
- Better organization for larger projects
- Demonstrates software architecture principles

Both versions provide identical functionality!

**Main Components**:
- **SnakeGame**: Main game class that handles:
  - Game initialization and setup
  - Snake movement and collision detection
  - Food generation
  - Rendering (drawing the snake, food, borders, score)
  - Input handling
  - Game state management
  - Game over logic

**For detailed architecture documentation, see [ARCHITECTURE.md](ARCHITECTURE.md)**

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

**Problem**: Game doesn't display correctly or crashes on startup.

**Solution**: Ensure your terminal window is large enough:
- **Minimum**: 80 columns × 24 rows
- **Recommended**: 100 columns × 30 rows or larger

To check your terminal size:
```bash
# Unix/Linux/macOS
echo "Columns: $(tput cols), Rows: $(tput lines)"

# Windows PowerShell
echo "Columns: $Host.UI.RawUI.WindowSize.Width, Rows: $Host.UI.RawUI.WindowSize.Height"
```

### Windows issues

**Problem**: "No module named '_curses'" or curses-related errors on Windows.

**Solution**: Install the `windows-curses` package:

```bash
pip install windows-curses
```

If you still have issues, try:
```bash
pip uninstall windows-curses
pip install --upgrade windows-curses
```

### Curses not available on Unix/Linux

**Problem**: "No module named '_curses'" error on Unix/Linux.

**Solution**: Install Python development headers:

```bash
# On Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3-dev

# On Fedora/RHEL/CentOS
sudo yum install python3-devel

# On Arch Linux
sudo pacman -S python

# On macOS
# curses should be included by default with Python
```

### Python version issues

**Problem**: Game doesn't run or has import errors.

**Solution**: Ensure you're using Python 3.8.1 or higher:

```bash
python --version
# or
python3 --version
```

If your version is older, install a newer version from [python.org](https://www.python.org/downloads/).

### Performance issues

**Problem**: Game is laggy or unresponsive.

**Solutions**:
- Close other applications consuming CPU/memory
- Use a lightweight terminal emulator (e.g., xterm on Linux)
- Reduce terminal font size slightly
- Ensure your terminal supports hardware acceleration

### Score file issues

**Problem**: High score not saving or loading.

**Details**: High score is saved to `~/.snake_game_high_score.json`

**Solution**: Check file permissions:
```bash
# Unix/Linux/macOS
ls -l ~/.snake_game_high_score.json
chmod 644 ~/.snake_game_high_score.json
```

### Keys not responding

**Problem**: Arrow keys or other controls don't work.

**Solutions**:
- Make sure the terminal window has focus
- Check if your terminal emulator supports arrow keys in curses mode
- Try a different terminal emulator
- On some systems, NumLock state might affect arrow keys

### Game exits immediately

**Problem**: Game starts and exits right away.

**Solutions**:
- Check terminal size (must be at least 80×24)
- Ensure Python curses module is properly installed
- Run the test suite: `python test_game.py`
- Check error messages in the terminal

### Still having issues?

If none of these solutions work:
1. Run the test suite: `python test_game.py`
2. Check the [Issues](https://github.com/thiyagij/python_snake_game/issues) page
3. Create a new issue with:
   - Your OS and version
   - Python version
   - Terminal emulator
   - Error messages
   - Output from test_game.py

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
