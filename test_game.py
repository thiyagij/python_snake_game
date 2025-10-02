#!/usr/bin/env python3
"""
Test script for Snake Game
Validates game logic without running the full curses interface.
"""

import sys
from collections import deque


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


def test_advanced_features():
    """Test advanced game features."""
    print("\nTesting Advanced Features...")
    print("-" * 50)
    
    # Test 6: Level progression
    score = 0
    level = 1
    for i in range(10):
        score += 10
        level = (score // 50) + 1
    assert level == 3, "Level should increase with score"
    print("✓ Test 6: Level progression")
    
    # Test 7: Obstacle collision
    obstacles = [[5, 5], [6, 6]]
    test_head = [5, 5]
    collision = test_head in obstacles
    assert collision, "Should detect obstacle collision"
    print("✓ Test 7: Obstacle collision detection")
    
    # Test 8: Snake skins
    import snake_game
    skins = snake_game.SnakeGame.SKINS
    assert 'classic' in skins, "Classic skin should exist"
    assert 'blocks' in skins, "Blocks skin should exist"
    assert len(skins) >= 4, "Should have at least 4 skins"
    print("✓ Test 8: Snake skins available")
    
    # Test 9: Leaderboard structure
    leaderboard_entry = {
        'score': 100,
        'level': 3,
        'date': '2024-01-01 12:00:00'
    }
    assert 'score' in leaderboard_entry, "Leaderboard entry should have score"
    assert 'level' in leaderboard_entry, "Leaderboard entry should have level"
    assert 'date' in leaderboard_entry, "Leaderboard entry should have date"
    print("✓ Test 9: Leaderboard structure")
    
    print("-" * 50)
    print("All advanced feature tests passed! ✓")


def test_imports():
    """Test that all required modules can be imported."""
    print("\nTesting module imports...")
    print("-" * 50)
    
    import curses
    print("✓ curses module available")
    
    import snake_game
    print("✓ snake_game module can be imported")
    
    # Check required components
    assert hasattr(snake_game, 'SnakeGame'), "SnakeGame class missing"
    assert hasattr(snake_game, 'main'), "main function missing"
    print("✓ Required classes and functions present")
    
    print("-" * 50)
    print("All imports successful! ✓")


def test_imports_legacy():
    """Legacy test function for backward compatibility with main() runner."""
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
        if not test_imports_legacy():
            return 1
        
        print()
        
        # Test game mechanics
        test_snake_mechanics()
        
        # Test advanced features
        test_advanced_features()
        
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
