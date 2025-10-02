#!/usr/bin/env python3
"""
2D Snake Game - Terminal Based
A classic snake game implementation using Python's curses library.
"""

import curses
import random
import json
import os
from collections import deque
from datetime import datetime


class SnakeGame:
    """Main Snake Game class handling game logic and rendering."""
    
    # Snake skin options
    SKINS = {
        'classic': {'head': 'O', 'body': 'o'},
        'blocks': {'head': '█', 'body': '▓'},
        'arrows': {'head': '>', 'body': '-'},
        'dots': {'head': '●', 'body': '○'}
    }
    
    def __init__(self, stdscr):
        """Initialize the game with curses screen."""
        self.stdscr = stdscr
        self.score = 0
        self.high_score = 0
        self.level = 1
        self.obstacles = []
        self.current_skin = 'classic'
        self.paused = False
        self.leaderboard_file = os.path.expanduser('~/.snake_game_leaderboard.json')
        
        # Load leaderboard
        self.leaderboard = self.load_leaderboard()
        if self.leaderboard:
            self.high_score = self.leaderboard[0]['score']
        
        # Setup curses
        curses.curs_set(0)  # Hide cursor
        self.stdscr.nodelay(1)  # Non-blocking input
        self.base_timeout = 100  # Base refresh rate in ms
        self.stdscr.timeout(self.base_timeout)
        
        # Get screen dimensions
        self.height, self.width = stdscr.getmaxyx()
        
        # Create game window
        self.game_height = self.height - 5
        self.game_width = self.width - 2
        self.window = curses.newwin(self.game_height, self.game_width, 2, 1)
        self.window.keypad(1)
        self.window.timeout(self.base_timeout)
        
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
        
        # Reset game state
        self.score = 0
        self.level = 1
        self.paused = False
        self.obstacles = []
        
        # Generate first food
        self.food = self.generate_food()
        
        # Update game speed
        self.update_speed()
    
    def update_speed(self):
        """Update game speed based on level."""
        # Speed increases with level (timeout decreases)
        timeout = max(50, self.base_timeout - (self.level - 1) * 10)
        self.window.timeout(timeout)
        self.stdscr.timeout(timeout)
    
    def calculate_level(self):
        """Calculate current level based on score."""
        new_level = (self.score // 50) + 1
        if new_level > self.level:
            self.level = new_level
            self.update_speed()
            self.add_obstacles()
    
    def add_obstacles(self):
        """Add obstacles as level increases."""
        # Add obstacles starting from level 3
        if self.level >= 3 and len(self.obstacles) < (self.level - 2) * 2:
            for _ in range(2):
                obstacle = self.generate_obstacle()
                if obstacle:
                    self.obstacles.append(obstacle)
    
    def generate_obstacle(self):
        """Generate an obstacle at a random position."""
        max_attempts = 100
        for _ in range(max_attempts):
            obs_y = random.randint(2, self.game_height - 3)
            obs_x = random.randint(2, self.game_width - 3)
            obstacle = [obs_y, obs_x]
            
            # Check if position is clear
            if (obstacle not in self.snake and 
                obstacle != self.food and 
                obstacle not in self.obstacles):
                return obstacle
        return None
    
    def load_leaderboard(self):
        """Load leaderboard from file."""
        try:
            if os.path.exists(self.leaderboard_file):
                with open(self.leaderboard_file, 'r') as f:
                    return json.load(f)
        except Exception:
            pass
        return []
    
    def save_leaderboard(self):
        """Save leaderboard to file."""
        try:
            with open(self.leaderboard_file, 'w') as f:
                json.dump(self.leaderboard, f, indent=2)
        except Exception:
            pass
    
    def update_leaderboard(self, score):
        """Update leaderboard with new score."""
        entry = {
            'score': score,
            'level': self.level,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        self.leaderboard.append(entry)
        self.leaderboard.sort(key=lambda x: x['score'], reverse=True)
        self.leaderboard = self.leaderboard[:10]  # Keep top 10
        self.save_leaderboard()
        
        if score > self.high_score:
            self.high_score = score
        
    def generate_food(self):
        """Generate food at a random position not occupied by snake or obstacles."""
        max_attempts = 1000
        for _ in range(max_attempts):
            food_y = random.randint(1, self.game_height - 2)
            food_x = random.randint(1, self.game_width - 2)
            food = [food_y, food_x]
            
            if food not in self.snake and food not in self.obstacles:
                return food
        # Fallback: return any valid position
        return [self.game_height // 2, self.game_width // 2]
    
    def draw_border(self):
        """Draw game border and title."""
        # Title
        title = " SNAKE GAME "
        self.stdscr.addstr(0, self.width // 2 - len(title) // 2, title, curses.A_BOLD)
        
        # Instructions
        instructions = "Arrow Keys | Q: Quit | R: Restart | P: Pause | S: Skin"
        self.stdscr.addstr(1, self.width // 2 - len(instructions) // 2, instructions)
        
        # Score and level
        score_text = f"Score: {self.score} | Level: {self.level} | Skin: {self.current_skin}"
        self.stdscr.addstr(self.height - 2, 2, score_text)
        
        high_score_text = f"High Score: {self.high_score}"
        self.stdscr.addstr(self.height - 2, self.width - len(high_score_text) - 2, high_score_text)
        
        # Draw border
        self.window.border()
        
        # Show pause indicator if paused
        if self.paused:
            pause_text = "*** PAUSED ***"
            self.stdscr.addstr(self.height - 1, self.width // 2 - len(pause_text) // 2, pause_text, curses.A_BOLD)
        
    def draw_snake(self):
        """Draw the snake on the screen."""
        skin = self.SKINS[self.current_skin]
        for i, segment in enumerate(self.snake):
            y, x = segment
            if i == 0:
                # Head of snake
                self.window.addch(y, x, skin['head'], curses.A_BOLD)
            else:
                # Body of snake
                self.window.addch(y, x, skin['body'])
    
    def draw_obstacles(self):
        """Draw obstacles on the screen."""
        for obstacle in self.obstacles:
            y, x = obstacle
            self.window.addch(y, x, '#', curses.A_BOLD)
    
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
        
        # Check for pause
        if key in [ord('p'), ord('P')]:
            self.paused = not self.paused
            return True
        
        # Check for skin change
        if key in [ord('s'), ord('S')]:
            self.change_skin()
            return True
        
        # Check for leaderboard view
        if key in [ord('l'), ord('L')]:
            self.show_leaderboard()
            return True
        
        # Update direction (prevent 180-degree turns) only if not paused
        if not self.paused and key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
            if (key == curses.KEY_UP and self.last_direction != curses.KEY_DOWN) or \
               (key == curses.KEY_DOWN and self.last_direction != curses.KEY_UP) or \
               (key == curses.KEY_LEFT and self.last_direction != curses.KEY_RIGHT) or \
               (key == curses.KEY_RIGHT and self.last_direction != curses.KEY_LEFT):
                self.direction = key
        
        return True
    
    def change_skin(self):
        """Cycle through available skins."""
        skins = list(self.SKINS.keys())
        current_index = skins.index(self.current_skin)
        self.current_skin = skins[(current_index + 1) % len(skins)]
    
    def show_leaderboard(self):
        """Display the leaderboard."""
        self.window.clear()
        self.window.border()
        
        title = "=== LEADERBOARD (Top 10) ==="
        self.window.addstr(2, self.game_width // 2 - len(title) // 2, title, curses.A_BOLD)
        
        if not self.leaderboard:
            no_scores = "No scores yet!"
            self.window.addstr(4, self.game_width // 2 - len(no_scores) // 2, no_scores)
        else:
            for i, entry in enumerate(self.leaderboard[:10]):
                score_line = f"{i+1:2d}. Score: {entry['score']:4d} | Level: {entry['level']:2d} | {entry['date']}"
                if i + 4 < self.game_height - 2:
                    self.window.addstr(i + 4, 3, score_line)
        
        instruction = "Press any key to continue..."
        self.window.addstr(self.game_height - 3, self.game_width // 2 - len(instruction) // 2, instruction)
        
        self.window.refresh()
        self.window.nodelay(0)
        self.window.getch()
        self.window.nodelay(1)
    
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
        """Check if snake collided with wall, itself, or obstacles."""
        y, x = head
        
        # Check wall collision
        if y <= 0 or y >= self.game_height - 1 or x <= 0 or x >= self.game_width - 1:
            return True
        
        # Check self collision
        if head in self.snake:
            return True
        
        # Check obstacle collision
        if head in self.obstacles:
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
            self.score += 10
            self.food = self.generate_food()
            # Calculate level progression
            self.calculate_level()
            # Snake grows (don't remove tail)
        else:
            # Remove tail (snake moves)
            self.snake.pop()
        
        # Update last direction
        self.last_direction = self.direction
        
        return True
    
    def game_over_screen(self):
        """Display game over screen."""
        # Update leaderboard
        self.update_leaderboard(self.score)
        
        self.window.clear()
        self.window.border()
        
        game_over_text = "GAME OVER!"
        final_score_text = f"Final Score: {self.score} | Level: {self.level}"
        
        mid_y = self.game_height // 2
        mid_x = self.game_width // 2
        
        self.window.addstr(mid_y - 2, mid_x - len(game_over_text) // 2, game_over_text, curses.A_BOLD)
        self.window.addstr(mid_y, mid_x - len(final_score_text) // 2, final_score_text)
        
        # Check if it's a high score
        if self.score == self.high_score and self.score > 0:
            new_high_score_text = "NEW HIGH SCORE!"
            self.window.addstr(mid_y + 1, mid_x - len(new_high_score_text) // 2, new_high_score_text, curses.A_BOLD)
        
        restart_text = "R: Restart | L: Leaderboard | Q: Quit"
        self.window.addstr(mid_y + 3, mid_x - len(restart_text) // 2, restart_text)
        
        self.window.refresh()
        
        # Wait for R, L, or Q
        self.window.nodelay(0)  # Blocking input
        while True:
            key = self.window.getch()
            if key in [ord('r'), ord('R')]:
                self.window.nodelay(1)  # Non-blocking input
                self.reset_game()
                return True
            elif key in [ord('l'), ord('L')]:
                self.show_leaderboard()
                # Redraw game over screen after leaderboard
                self.window.clear()
                self.window.border()
                self.window.addstr(mid_y - 2, mid_x - len(game_over_text) // 2, game_over_text, curses.A_BOLD)
                self.window.addstr(mid_y, mid_x - len(final_score_text) // 2, final_score_text)
                if self.score == self.high_score and self.score > 0:
                    new_high_score_text = "NEW HIGH SCORE!"
                    self.window.addstr(mid_y + 1, mid_x - len(new_high_score_text) // 2, new_high_score_text, curses.A_BOLD)
                self.window.addstr(mid_y + 3, mid_x - len(restart_text) // 2, restart_text)
                self.window.refresh()
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
            self.draw_obstacles()
            
            # Refresh
            self.stdscr.refresh()
            self.window.refresh()
            
            # Get input
            if not self.get_input():
                break
            
            # Update game state
            if not self.update():
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
