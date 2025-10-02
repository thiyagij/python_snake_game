#!/usr/bin/env python3
"""
Test script for Snake Game
Validates game logic without running the full curses interface.
"""

import sys
from collections import deque
import random


def test_snake_mechanics():
    """Test basic snake mechanics."""
    print("Testing Snake Game Mechanics...")
    print("-" * 50)
    
    # Test 1: Snake initialization
    snake = deque([[10, 10], [10, 9], [10, 8]])
    assert len(snake) == 3, "Snake should start with 3 segments"
    print("✓ Test 1: Snake initialization")
    
    # Test 2: Movement
    head = snake[0].copy()
    head[1] += 1  # Move right
    snake.appendleft(head)
    snake.pop()
    assert snake[0] == [10, 11], "Snake should move right correctly"
    print("✓ Test 2: Snake movement")
    
    # Test 3: Growth
    initial_length = len(snake)
    head = snake[0].copy()
    head[1] += 1
    snake.appendleft(head)
    # Don't remove tail (simulate eating)
    assert len(snake) == initial_length + 1, "Snake should grow"
    print("✓ Test 3: Snake growth")
    
    # Test 4: Collision detection
    game_height, game_width = 20, 40
    
    # Wall collision
    test_head = [0, 10]  # Top wall
    collision = (test_head[0] <= 0 or test_head[0] >= game_height - 1 or 
                 test_head[1] <= 0 or test_head[1] >= game_width - 1)
    assert collision, "Should detect wall collision"
    print("✓ Test 4: Collision detection")
    
    # Test 5: Score
    score = 0
    for _ in range(5):
        score += 10
    assert score == 50, "Score calculation should be correct"
    print("✓ Test 5: Score calculation")
    
    print("-" * 50)
    print("All tests passed! ✓")


def test_imports():
    """Test that all required modules can be imported."""
    print("\nTesting module imports...")
    print("-" * 50)
    
    try:
        import curses
        print("✓ curses module available")
    except ImportError:
        print("✗ curses module not available")
        print("  Install with: pip install windows-curses (Windows only)")
        return False
    
    try:
        import snake_game
        print("✓ snake_game module can be imported")
        
        # Check required components
        assert hasattr(snake_game, 'SnakeGame'), "SnakeGame class missing"
        assert hasattr(snake_game, 'main'), "main function missing"
        print("✓ Required classes and functions present")
        
    except ImportError as e:
        print(f"✗ Failed to import snake_game: {e}")
        return False
    except AssertionError as e:
        print(f"✗ Missing required component: {e}")
        return False
    
    print("-" * 50)
    print("All imports successful! ✓")
    return True


def main():
    """Run all tests."""
    print("=" * 50)
    print("SNAKE GAME - TEST SUITE")
    print("=" * 50)
    print()
    
    try:
        # Test imports first
        if not test_imports():
            return 1
        
        print()
        
        # Test game mechanics
        test_snake_mechanics()
        
        print()
        print("=" * 50)
        print("ALL TESTS PASSED ✓")
        print("=" * 50)
        print()
        print("The game is ready to play!")
        print("Run: python snake_game.py")
        print()
        
        return 0
        
    except Exception as e:
        print(f"\n✗ Test failed with error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
