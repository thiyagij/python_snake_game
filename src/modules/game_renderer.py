"""
Game Renderer Module
Handles all drawing and display operations.
"""

import curses
from .game_config import SNAKE_HEAD_CHAR, SNAKE_BODY_CHAR, FOOD_CHAR


class GameRenderer:
    """Handles rendering of game elements."""

    def __init__(self, stdscr, window, game_height, game_width):
        """Initialize renderer with screen and window references."""
        self.stdscr = stdscr
        self.window = window
        self.game_height = game_height
        self.game_width = game_width
        self.height, self.width = stdscr.getmaxyx()

    def draw_border(self, score, high_score, paused):
        """Draw game border, title, and score."""
        # Title
        title = " SNAKE GAME "
        self.stdscr.addstr(0, self.width // 2 - len(title) // 2, title, curses.A_BOLD)

        # Instructions
        instructions = "Arrow Keys: Move | P: Pause | R: Restart | Q: Quit"
        self.stdscr.addstr(1, self.width // 2 - len(instructions) // 2, instructions)

        # Score
        score_text = f"Score: {score}"
        self.stdscr.addstr(self.height - 2, 2, score_text)

        high_score_text = f"High Score: {high_score}"
        self.stdscr.addstr(self.height - 2, self.width - len(high_score_text) - 2, high_score_text)

        # Pause indicator
        if paused:
            pause_text = "*** PAUSED ***"
            self.stdscr.addstr(self.height - 1, self.width // 2 - len(pause_text) // 2, pause_text, curses.A_BOLD)

        # Draw border
        self.window.border()

    def draw_snake(self, snake):
        """Draw the snake on the screen."""
        for i, segment in enumerate(snake):
            y, x = segment
            if i == 0:
                # Head of snake
                self.window.addch(y, x, SNAKE_HEAD_CHAR, curses.A_BOLD)
            else:
                # Body of snake
                self.window.addch(y, x, SNAKE_BODY_CHAR)

    def draw_food(self, food):
        """Draw food on the screen."""
        y, x = food
        self.window.addch(y, x, FOOD_CHAR, curses.A_BOLD)

    def draw_game_over(self, score):
        """Display game over screen."""
        self.window.clear()
        self.window.border()

        game_over_text = "GAME OVER!"
        final_score_text = f"Final Score: {score}"
        restart_text = "Press R to restart or Q to quit"

        mid_y = self.game_height // 2
        mid_x = self.game_width // 2

        self.window.addstr(mid_y - 1, mid_x - len(game_over_text) // 2, game_over_text, curses.A_BOLD)
        self.window.addstr(mid_y, mid_x - len(final_score_text) // 2, final_score_text)
        self.window.addstr(mid_y + 2, mid_x - len(restart_text) // 2, restart_text)

        self.window.refresh()
