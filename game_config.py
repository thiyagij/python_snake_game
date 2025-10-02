"""
Game Configuration Module
Contains constants and configuration for the Snake Game.
"""

import os

# Game Settings
REFRESH_RATE_MS = 100  # Game refresh rate in milliseconds
INITIAL_SNAKE_LENGTH = 3  # Starting length of the snake
FOOD_POINTS = 10  # Points awarded for eating food

# Display Characters
SNAKE_HEAD_CHAR = 'O'
SNAKE_BODY_CHAR = 'o'
FOOD_CHAR = '*'

# File Paths
SCORE_FILE = os.path.expanduser("~/.snake_game_high_score.json")

# Game Window Settings
WINDOW_MARGIN_TOP = 2
WINDOW_MARGIN_BOTTOM = 5
WINDOW_MARGIN_HORIZONTAL = 2
