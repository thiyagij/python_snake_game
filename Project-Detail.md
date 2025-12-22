# Project Detail — Python Snake Game

> Generated on: 2025-12-22

## 1) What this project is

This repository contains a **terminal-based Snake game** implemented in Python using the `curses` library.

It ships **two playable implementations**:

1. **Monolithic / feature-rich version**: `src/snake_game.py`
   - Includes advanced gameplay features: **levels, speed progression, obstacles, skins, and a top-10 leaderboard**.

2. **Modular / refactored version**: `src/snake_game_modular.py` + `src/modules/*`
   - Demonstrates separation of concerns (config, rendering, persistence).
   - Implements **core Snake gameplay** and **persistent high score**, but does **not** include the monolithic version’s level/obstacle/skin/leaderboard system.

## 2) Repository structure

Top-level layout (key files):

- `README.md` — overview, installation, controls, screenshots
- `pyproject.toml` — Poetry config, dependencies, tool configs, script entrypoint
- `requirements.txt` — minimal pip requirements (primarily `windows-curses` on Windows)
- `setup.sh` / `setup.bat` — convenience setup scripts
- `docs/` — architecture, features, gameplay, quickstart, CI/CD docs
- `src/`
  - `snake_game.py` — monolithic game
  - `snake_game_modular.py` — modular game
  - `modules/`
    - `game_config.py` — constants
    - `game_renderer.py` — drawing/UI
    - `score_manager.py` — high score persistence
- `tests/test_game.py` — lightweight logic + import test suite (non-curses)

## 3) Requirements and platform notes

### Python
- Python **3.8.1+** (declared in `pyproject.toml`).

### Curses
- On **Linux/macOS**, `curses` comes with Python.
- On **Windows**, the project relies on `windows-curses`.
  - Poetry: `windows-curses` is included via an OS marker.
  - Pip: `requirements.txt` includes it only when `sys_platform == 'win32'`.

### Terminal
- Best experience with a terminal size of at least **80×24**.

## 4) How to run

### Run directly with Python
- Monolithic version:
  - `python src/snake_game.py`
- Modular version:
  - `python src/snake_game_modular.py`

### Run via Poetry
- Install dependencies: `poetry install`
- Run the script entrypoint: `poetry run snake-game`
  - This maps to: `src.snake_game:main_wrapper`

## 5) Controls and gameplay

### Controls (monolithic version: `src/snake_game.py`)
- Arrow keys: move
- `P`: pause/resume
- `R`: restart
- `Q`: quit
- `S`: cycle snake skin
- `L`: show leaderboard

### Controls (modular version: `src/snake_game_modular.py`)
- Arrow keys: move
- `P`: pause/resume
- `R`: restart
- `Q`: quit

### Core rules (both versions)
- The snake continuously moves in its current direction.
- Eating food increases score and grows the snake.
- Game ends on collision with walls or the snake body.

## 6) The monolithic implementation (feature-rich)

File: `src/snake_game.py`

### Main class
- `class SnakeGame` owns both **game state** and **presentation**.

### Key state fields
- `self.snake`: `collections.deque` of `[y, x]` segments (head at index 0)
- `self.food`: `[y, x]`
- `self.score`, `self.high_score`
- `self.level`: derived from score (see level system below)
- `self.obstacles`: list of `[y, x]` positions
- `self.current_skin`: key into `SKINS`
- `self.paused`: boolean
- `self.leaderboard`: list of leaderboard entries
- `self.leaderboard_file`: `~/.snake_game_leaderboard.json`

### Rendering
The monolithic version draws everything directly:
- Title + instructions at top
- A bordered playfield (`self.window.border()`)
- Snake head/body using the currently selected skin
- Food (`*`)
- Obstacles (`#`)
- Score, level, skin name, and high score

### Input handling
- Reads key presses from the game window.
- Prevents 180° turns by tracking `self.last_direction`.
- Implements action keys (`P`, `R`, `Q`, `S`, `L`).

### Movement and collision
- `move_snake()` computes the next head coordinate based on direction.
- `check_collision(head)` checks:
  - wall collision
  - self collision
  - obstacle collision

### Scoring
- Each food eaten adds **10 points**.

### Level system and speed progression
- Level is computed as:
  - `level = (score // 50) + 1`
- Each level update reduces input timeout (game speed increases):
  - base timeout is `100ms`
  - each level reduces by `10ms`
  - minimum is clamped at `50ms`

### Dynamic obstacles
- Obstacles begin at **level 3**.
- When the player reaches a new level, `add_obstacles()` attempts to add obstacles.
- The implementation maintains a cap based on level:
  - up to `(level - 2) * 2` total obstacles
  - added in batches of 2 when progressing
- Obstacles are generated randomly while avoiding snake, food, and existing obstacles.

### Skins
- `SnakeGame.SKINS` defines 4 skins:
  - classic: `O` / `o`
  - blocks: `█` / `▓`
  - arrows: `>` / `-`
  - dots: `●` / `○`
- Press `S` to cycle skins during play.

### Leaderboard persistence
- Stored at: `~/.snake_game_leaderboard.json`
- On game over, the score is appended and the list is:
  - sorted descending by score
  - truncated to the top 10
- Each entry includes:
  - `score`
  - `level`
  - `date` timestamp string
- Press `L` during gameplay or at game-over to view the leaderboard.

### Main loop
- `run()` repeatedly:
  1. clears screen
  2. draws UI + game objects
  3. reads input
  4. updates game state
  5. transitions to game-over screen on collision

### Entry point
- `main_wrapper()` calls `curses.wrapper(main)` and prints a friendly message on keyboard interrupt.

## 7) The modular implementation (separation of concerns)

File: `src/snake_game_modular.py`

### Goal
This version is structured as an example of maintainable architecture:
- configuration constants live in one module
- rendering is in one module
- persistence is in one module
- the main game file orchestrates them

### Modules

#### `src/modules/game_config.py`
Provides constants:
- refresh rate (`REFRESH_RATE_MS`)
- initial snake length / scoring (`INITIAL_SNAKE_LENGTH`, `FOOD_POINTS`)
- display characters (`SNAKE_HEAD_CHAR`, `SNAKE_BODY_CHAR`, `FOOD_CHAR`)
- the high score file path (`SCORE_FILE` → `~/.snake_game_high_score.json`)
- window margins used when sizing the curses window

#### `src/modules/score_manager.py`
Defines `ScoreManager`:
- `load_high_score()` reads JSON if present and returns `high_score` (default 0)
- `save_high_score(score)` writes `{"high_score": score}` as JSON
- errors are swallowed (fail-safe gameplay; persistence is best-effort)

#### `src/modules/game_renderer.py`
Defines `GameRenderer`:
- draws border/title/instructions and score/high score
- draws snake and food
- draws pause indicator
- draws a simple game-over screen

### Main game logic (`snake_game_modular.py`)
- `SnakeGame` maintains:
  - `snake`, `food`, `score`, `high_score`, `paused`
- Collision checks only walls + self.
- When game ends:
  - updates high score if current score beats it
  - uses renderer’s game-over screen

### Note about imports
`snake_game_modular.py` alters `sys.path` to allow importing `modules.*` when running the file directly.

## 8) Persistence model (important difference between versions)

This repo currently stores scores in **two separate places**, depending on which version you run:

- Monolithic leaderboard:
  - File: `~/.snake_game_leaderboard.json`
  - Data: top 10 entries with score/level/date

- Modular high score:
  - File: `~/.snake_game_high_score.json`
  - Data: a single `high_score` integer

This means your scores do not “carry over” between versions unless the code is unified.

## 9) Testing

File: `tests/test_game.py`

This is a pragmatic, curses-free test script that validates:
- basic snake mechanics using a `deque`
- score arithmetic
- level progression formula
- obstacle collision concept
- skins dictionary exists and contains expected keys
- `curses` is importable (platform dependent)
- `src.snake_game` exports `SnakeGame` and `main`

Ways to run:
- `python tests/test_game.py`
- `pytest` (configured in `pyproject.toml`)

## 10) CI/CD (GitHub Actions)

Documentation: `docs/CI_CD.md`

Pipeline includes:
- **Lint**: flake8
- **Test**: matrix (OS: Ubuntu/Windows/macOS × Python 3.8–3.12)
- **Build**: Poetry build artifacts
- Optional publishing steps + GitHub Pages deployment for docs

Local equivalents:
- `flake8 .`
- `pytest -v --cov=src --cov-report=term-missing`
- `poetry build`

## 11) Packaging and dependencies

### Poetry
- Project metadata is in `pyproject.toml`.
- Script entrypoint:
  - `snake-game = "src.snake_game:main_wrapper"`

### Dependencies
- Runtime:
  - `windows-curses` only on Windows
- Dev:
  - `pytest`, `pytest-cov`, `flake8`

## 12) Where to extend the game

Depending on which version you’re extending:

- If you want gameplay features (levels, obstacles, skins, leaderboard), start from `src/snake_game.py`.
- If you want clean architecture, start from `src/snake_game_modular.py` and consider porting features across while keeping modules separated.

Common extension directions:
- additional obstacle patterns
- additional skins
- multiple food types / power-ups
- unified persistence between both versions

---

If you want, I can also:
- unify the persistence format so both versions share scores, or
- port the monolithic “advanced features” into the modular architecture.
