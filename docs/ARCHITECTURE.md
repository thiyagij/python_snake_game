# Architecture Documentation 🏗️

## Overview

The Python Snake Game is available in two versions:

1. **Monolithic Version** (`snake_game.py`) - Single-file implementation
2. **Modular Version** (`snake_game_modular.py`) - Refactored with separate modules

Both versions provide identical functionality and game experience.

## Modular Architecture

The modular version splits the code into logical components for better maintainability:

```
python_snake_game/
├── src/
│   ├── snake_game.py              # Original monolithic version
│   ├── snake_game_modular.py      # Modular version (main game)
│   └── modules/
│       ├── game_config.py         # Configuration constants
│       ├── score_manager.py       # High score persistence
│       └── game_renderer.py       # Display and rendering
└── tests/
    └── test_game.py               # Test suite
```

### Module Descriptions

#### `game_config.py`
**Purpose**: Central configuration for game constants

**Contains**:
- Game settings (refresh rate, initial snake length, points)
- Display characters (snake head, body, food)
- File paths (high score file location)
- Window margins and dimensions

**Why separate**: Makes it easy to adjust game parameters without touching game logic.

#### `score_manager.py`
**Purpose**: Handles high score persistence

**Key Class**: `ScoreManager`

**Responsibilities**:
- Load high score from JSON file
- Save high score to JSON file
- Handle file I/O errors gracefully

**Why separate**: Isolates file operations and makes it easy to change storage format.

#### `game_renderer.py`
**Purpose**: All display and drawing operations

**Key Class**: `GameRenderer`

**Responsibilities**:
- Draw game border, title, and instructions
- Draw snake (head and body)
- Draw food
- Draw score and high score
- Display pause indicator
- Render game over screen

**Why separate**: Separates presentation from game logic, making UI changes easier.

#### `snake_game_modular.py`
**Purpose**: Main game logic and orchestration

**Key Class**: `SnakeGame`

**Responsibilities**:
- Game state management
- Snake movement logic
- Collision detection
- Input handling
- Game loop orchestration
- Integration of all modules

**Why this approach**: Keeps the main game logic focused on behavior, delegating specific tasks to specialized modules.

## Design Principles

### 1. Single Responsibility Principle
Each module has one clear purpose:
- Configuration → `game_config.py`
- Persistence → `score_manager.py`
- Rendering → `game_renderer.py`
- Game Logic → `snake_game_modular.py`

### 2. Separation of Concerns
- **Display logic** is isolated from game logic
- **File I/O** is separated from game state
- **Configuration** is centralized

### 3. Backward Compatibility
- Original `snake_game.py` is unchanged and fully functional
- Both versions use the same game mechanics
- Tests work with both versions

### 4. Easy Testing
Modular structure makes it easier to:
- Test individual components
- Mock dependencies
- Isolate bugs

### 5. Maintainability
- Changes to rendering don't affect game logic
- Configuration changes are centralized
- Each module is small and focused

## Which Version to Use?

### Use `snake_game.py` if:
- You want a simple, single-file implementation
- You're learning Python and want to see everything in one place
- You want minimal dependencies

### Use `snake_game_modular.py` if:
- You're working on a team
- You plan to extend or customize the game
- You prefer organized, modular code
- You want to understand software architecture patterns

## Running the Modular Version

```bash
# Run the modular version
python src/snake_game_modular.py

# Or use the original version
python src/snake_game.py
```

Both versions provide identical gameplay and features!

## Testing

The test suite (`test_game.py`) works with both versions:

```bash
# Test original version
python tests/test_game.py

# Test modular components
python -c "import game_config; import score_manager; import game_renderer; print('All modules OK')"
```

## Future Enhancements

The modular structure makes it easy to add:

### Easy to Add
- **New game modes**: Extend `SnakeGame` class
- **Different renderers**: Create alternative `GameRenderer` implementations
- **Multiple storage backends**: Extend `ScoreManager` for database support
- **Power-ups and obstacles**: Add to game logic without touching rendering

### Examples of Extensions

#### Adding a Database Score Backend
```python
# score_manager_db.py
class DatabaseScoreManager(ScoreManager):
    def load_high_score(self):
        # Load from database
        pass
    
    def save_high_score(self, score):
        # Save to database
        pass
```

#### Adding Color Support
```python
# game_renderer_color.py
class ColorGameRenderer(GameRenderer):
    def draw_snake(self, snake):
        # Draw with colors
        pass
```

## Code Quality

Both versions follow:
- **PEP 8** style guidelines
- **Comprehensive docstrings**
- **Clear variable names**
- **Type hints** (can be added)
- **Error handling**

## Performance

- Both versions have identical performance
- No overhead from modular structure
- Same refresh rate and responsiveness

## Contributing

When contributing to the modular version:

1. Keep modules focused on their single responsibility
2. Update both versions if adding core features
3. Add tests for new functionality
4. Update this documentation for architectural changes

---

**Note**: The modular version demonstrates good software engineering practices while maintaining the simplicity and fun of the original game! 🐍🎮
