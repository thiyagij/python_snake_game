#!/usr/bin/env python3
"""
2D Snake Game - Terminal Based (Modular Version)
A classic snake game implementation using Python's curses library.
This is a refactored modular version that imports from separate modules.
"""

import curses
import random
from collections import deque

# Import modular components
from game_config import (
    REFRESH_RATE_MS, INITIAL_SNAKE_LENGTH, FOOD_POINTS,
    SCORE_FILE, WINDOW_MARGIN_TOP, WINDOW_MARGIN_BOTTOM, WINDOW_MARGIN_HORIZONTAL
)
from score_manager import ScoreManager
from game_renderer import GameRenderer


class SnakeGame:
    """Main Snake Game class handling game logic and rendering."""

    def __init__(self, stdscr):
        """Initialize the game with curses screen."""
        self.stdscr = stdscr
        self.score = 0
        self.paused = False

        # Initialize score manager
        self.score_manager = ScoreManager(SCORE_FILE)
        self.high_score = self.score_manager.load_high_score()

        # Setup curses
        curses.curs_set(0)  # Hide cursor
        self.stdscr.nodelay(1)  # Non-blocking input
        self.stdscr.timeout(REFRESH_RATE_MS)  # Refresh rate in ms

        # Get screen dimensions
        self.height, self.width = stdscr.getmaxyx()

        # Create game window
        self.game_height = self.height - WINDOW_MARGIN_BOTTOM
        self.game_width = self.width - WINDOW_MARGIN_HORIZONTAL
        self.window = curses.newwin(self.game_height, self.game_width, WINDOW_MARGIN_TOP, 1)
        self.window.keypad(1)
        self.window.timeout(REFRESH_RATE_MS)

        # Initialize renderer
        self.renderer = GameRenderer(self.stdscr, self.window, self.game_height, self.game_width)

        # Initialize game state
        self.reset_game()

    def reset_game(self):
        """Reset game state for a new game."""
        # Snake starts in the middle
        start_y = self.game_height // 2
        start_x = self.game_width // 2

        # Snake body (deque of [y, x] coordinates)
        self.snake = deque([
            [start_y, start_x],
            [start_y, start_x - 1],
            [start_y, start_x - 2]
        ])

        # Initial direction (right)
        self.direction = curses.KEY_RIGHT
        self.last_direction = self.direction

        # Generate first food
        self.food = self.generate_food()

        # Reset score
        self.score = 0

    def generate_food(self):
        """Generate food at a random position not occupied by snake."""
        while True:
            food_y = random.randint(1, self.game_height - 2)
            food_x = random.randint(1, self.game_width - 2)
            food = [food_y, food_x]

            if food not in self.snake:
                return food

    def get_input(self):
        """Get user input and update direction."""
        key = self.window.getch()

        # Check for quit
        if key in [ord('q'), ord('Q')]:
            return False

        # Check for pause/resume
        if key in [ord('p'), ord('P')]:
            self.paused = not self.paused
            return True

        # Check for restart
        if key in [ord('r'), ord('R')]:
            self.reset_game()
            return True

        # Don't update direction if paused
        if self.paused:
            return True

        # Update direction (prevent 180-degree turns)
        if key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
            if (key == curses.KEY_UP and self.last_direction != curses.KEY_DOWN) or \
               (key == curses.KEY_DOWN and self.last_direction != curses.KEY_UP) or \
               (key == curses.KEY_LEFT and self.last_direction != curses.KEY_RIGHT) or \
               (key == curses.KEY_RIGHT and self.last_direction != curses.KEY_LEFT):
                self.direction = key

        return True

    def move_snake(self):
        """Move snake in current direction."""
        head = self.snake[0].copy()

        # Calculate new head position
        if self.direction == curses.KEY_UP:
            head[0] -= 1
        elif self.direction == curses.KEY_DOWN:
            head[0] += 1
        elif self.direction == curses.KEY_LEFT:
            head[1] -= 1
        elif self.direction == curses.KEY_RIGHT:
            head[1] += 1

        return head

    def check_collision(self, head):
        """Check if snake collided with wall or itself."""
        y, x = head

        # Check wall collision
        if y <= 0 or y >= self.game_height - 1 or x <= 0 or x >= self.game_width - 1:
            return True

        # Check self collision
        if head in self.snake:
            return True

        return False

    def update(self):
        """Update game state."""
        # Don't update if paused
        if self.paused:
            return True

        new_head = self.move_snake()

        # Check collision
        if self.check_collision(new_head):
            return False

        # Add new head
        self.snake.appendleft(new_head)

        # Check if food eaten
        if new_head == self.food:
            self.score += FOOD_POINTS
            self.food = self.generate_food()
            # Snake grows (don't remove tail)
        else:
            # Remove tail (snake moves)
            self.snake.pop()

        # Update last direction
        self.last_direction = self.direction

        return True

    def game_over_screen(self):
        """Display game over screen and wait for input."""
        self.renderer.draw_game_over(self.score)

        # Wait for R or Q
        self.window.nodelay(0)  # Blocking input
        while True:
            key = self.window.getch()
            if key in [ord('r'), ord('R')]:
                self.window.nodelay(1)  # Non-blocking input
                self.reset_game()
                return True
            elif key in [ord('q'), ord('Q')]:
                return False

    def run(self):
        """Main game loop."""
        running = True

        while running:
            # Clear screen
            self.stdscr.clear()
            self.window.clear()

            # Draw everything
            self.renderer.draw_border(self.score, self.high_score, self.paused)
            self.renderer.draw_snake(self.snake)
            self.renderer.draw_food(self.food)

            # Refresh
            self.stdscr.refresh()
            self.window.refresh()

            # Get input
            if not self.get_input():
                break

            # Update game state
            if not self.update():
                # Update high score
                if self.score > self.high_score:
                    self.high_score = self.score
                    self.score_manager.save_high_score(self.high_score)

                # Game over
                if not self.game_over_screen():
                    break


def main(stdscr):
    """Main entry point for the game."""
    game = SnakeGame(stdscr)
    game.run()


def main_wrapper():
    """Wrapper function for poetry script entry point."""
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        print("\nGame terminated by user.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main_wrapper()
