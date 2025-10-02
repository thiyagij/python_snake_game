#!/usr/bin/env python3
"""
2D Snake Game - Terminal Based
A classic snake game implementation using Python's curses library.
"""

import curses
import random
from collections import deque


class SnakeGame:
    """Main Snake Game class handling game logic and rendering."""
    
    def __init__(self, stdscr):
        """Initialize the game with curses screen."""
        self.stdscr = stdscr
        self.score = 0
        self.high_score = 0
        
        # Setup curses
        curses.curs_set(0)  # Hide cursor
        self.stdscr.nodelay(1)  # Non-blocking input
        self.stdscr.timeout(100)  # Refresh rate in ms
        
        # Get screen dimensions
        self.height, self.width = stdscr.getmaxyx()
        
        # Create game window
        self.game_height = self.height - 5
        self.game_width = self.width - 2
        self.window = curses.newwin(self.game_height, self.game_width, 2, 1)
        self.window.keypad(1)
        self.window.timeout(100)
        
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
    
    def draw_border(self):
        """Draw game border and title."""
        # Title
        title = " SNAKE GAME "
        self.stdscr.addstr(0, self.width // 2 - len(title) // 2, title, curses.A_BOLD)
        
        # Instructions
        instructions = "Use Arrow Keys | Q: Quit | R: Restart"
        self.stdscr.addstr(1, self.width // 2 - len(instructions) // 2, instructions)
        
        # Score
        score_text = f"Score: {self.score}"
        self.stdscr.addstr(self.height - 2, 2, score_text)
        
        high_score_text = f"High Score: {self.high_score}"
        self.stdscr.addstr(self.height - 2, self.width - len(high_score_text) - 2, high_score_text)
        
        # Draw border
        self.window.border()
        
    def draw_snake(self):
        """Draw the snake on the screen."""
        for i, segment in enumerate(self.snake):
            y, x = segment
            if i == 0:
                # Head of snake
                self.window.addch(y, x, 'O', curses.A_BOLD)
            else:
                # Body of snake
                self.window.addch(y, x, 'o')
    
    def draw_food(self):
        """Draw food on the screen."""
        y, x = self.food
        self.window.addch(y, x, '*', curses.A_BOLD)
    
    def get_input(self):
        """Get user input and update direction."""
        key = self.window.getch()
        
        # Check for quit
        if key in [ord('q'), ord('Q')]:
            return False
            
        # Check for restart
        if key in [ord('r'), ord('R')]:
            self.reset_game()
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
        new_head = self.move_snake()
        
        # Check collision
        if self.check_collision(new_head):
            return False
        
        # Add new head
        self.snake.appendleft(new_head)
        
        # Check if food eaten
        if new_head == self.food:
            self.score += 10
            self.food = self.generate_food()
            # Snake grows (don't remove tail)
        else:
            # Remove tail (snake moves)
            self.snake.pop()
        
        # Update last direction
        self.last_direction = self.direction
        
        return True
    
    def game_over_screen(self):
        """Display game over screen."""
        self.window.clear()
        self.window.border()
        
        game_over_text = "GAME OVER!"
        final_score_text = f"Final Score: {self.score}"
        restart_text = "Press R to restart or Q to quit"
        
        mid_y = self.game_height // 2
        mid_x = self.game_width // 2
        
        self.window.addstr(mid_y - 1, mid_x - len(game_over_text) // 2, game_over_text, curses.A_BOLD)
        self.window.addstr(mid_y, mid_x - len(final_score_text) // 2, final_score_text)
        self.window.addstr(mid_y + 2, mid_x - len(restart_text) // 2, restart_text)
        
        self.window.refresh()
        
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
            self.draw_border()
            self.draw_snake()
            self.draw_food()
            
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
