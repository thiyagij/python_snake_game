# Advanced Features 🎮✨

This document describes the advanced features added to the Snake Game in Step 9 of the improvement plan.

## Overview

The Snake Game now includes several advanced features that enhance gameplay, increase difficulty progressively, and provide better player experience through customization and score tracking.

## Feature List

### 1. Progressive Level System 📊

The game now includes a dynamic level system that increases difficulty as you progress.

**How it works:**
- Start at Level 1
- Every 50 points earned advances you to the next level
- Game speed increases with each level
- Visual level indicator in the UI

**Level Progression:**
- Level 1: Score 0-49
- Level 2: Score 50-99
- Level 3: Score 100-149
- And so on...

**Benefits:**
- Provides a sense of progression
- Increases challenge gradually
- Rewards skillful play

### 2. Dynamic Obstacles 🧱

Obstacles add a new layer of challenge to the game.

**How it works:**
- Obstacles (`#`) appear starting at Level 3
- Each level adds 2 more obstacles
- Obstacles are randomly placed on the game board
- Hitting an obstacle = Game Over

**Obstacle Progression:**
- Level 1-2: No obstacles
- Level 3: 2 obstacles
- Level 4: 4 obstacles
- Level 5: 6 obstacles
- And so on...

**Strategy Tips:**
- Plan your path around obstacles
- Use the space wisely
- Obstacles make the game increasingly challenging

### 3. Multiple Snake Skins 🎨

Customize your snake's appearance with different visual styles.

**Available Skins:**

1. **Classic** (Default)
   - Head: `O`
   - Body: `o`
   - Traditional snake appearance

2. **Blocks**
   - Head: `█`
   - Body: `▓`
   - Solid block style for better visibility

3. **Arrows**
   - Head: `>`
   - Body: `-`
   - Directional arrow style

4. **Dots**
   - Head: `●`
   - Body: `○`
   - Circular dot style

**How to Change Skins:**
- Press `S` during gameplay
- Cycles through all available skins
- Change persists for the current session
- No gameplay impact, purely cosmetic

### 4. Persistent Leaderboard 🏆

Your top scores are now saved permanently!

**Features:**
- Stores top 10 scores
- Persists across game sessions
- Saved to `~/.snake_game_leaderboard.json`

**Leaderboard Entry Includes:**
- Rank (1-10)
- Score
- Level reached
- Date and time achieved

**How to View:**
- Press `L` during gameplay
- Press `L` at game over screen
- Automatically updated when game ends

**Example Leaderboard:**
```
=== LEADERBOARD (Top 10) ===

 1. Score:  280 | Level:  6 | 2024-01-15 14:23:45
 2. Score:  190 | Level:  4 | 2024-01-15 13:15:22
 3. Score:  150 | Level:  3 | 2024-01-14 18:45:10
 ...
```

### 5. Pause/Resume Functionality ⏸️

Take a break without ending your game!

**Features:**
- Press `P` to pause
- Press `P` again to resume
- Game state is completely frozen while paused
- Visual pause indicator displayed
- No time limit on pause

**Benefits:**
- Take breaks during long games
- Plan your next moves
- No pressure to keep playing continuously

## Complete Controls Reference

| Key | Action |
|-----|--------|
| ↑↓←→ | Move snake direction |
| P | Pause/Resume game |
| S | Change snake skin |
| L | View leaderboard |
| R | Restart game |
| Q | Quit game |

## Gameplay Enhancements

### Score Display
The game now shows:
- Current score
- Current level
- Current skin name
- All-time high score (from leaderboard)

### Speed Progression
- Base speed: 100ms refresh rate
- Speed increase: 10ms faster per level
- Minimum speed: 50ms (max difficulty at level 6+)
- Creates increasing challenge

### Food Generation
- Improved algorithm to avoid obstacles
- Ensures food never spawns on snake or obstacles
- Fallback mechanism if no valid position found

## Technical Details

### File Storage
- Leaderboard: `~/.snake_game_leaderboard.json`
- Format: JSON with score, level, and timestamp
- Maximum entries: 10 (top scores only)

### Performance
- Efficient obstacle collision detection
- Optimized food generation algorithm
- No performance impact from new features

### Compatibility
- All features work on all supported platforms
- No additional dependencies required
- Backward compatible with existing saves

## Future Enhancements

Potential future additions:
- [ ] Multiple difficulty modes
- [ ] Power-ups and special foods
- [ ] Different game modes (timed, survival, etc.)
- [ ] Online leaderboard
- [ ] Custom obstacle patterns
- [ ] Sound effects
- [ ] Color themes

## Testing

All features have been thoroughly tested:
- Unit tests for level progression
- Obstacle collision detection tests
- Skin system tests
- Leaderboard structure tests
- All tests pass with pytest and direct Python

## Visual Examples

### Example 1: Early Game (Level 1, Classic Skin)
```
                           SNAKE GAME
    Arrow Keys | Q: Quit | R: Restart | P: Pause | S: Skin

┌────────────────────────────────────────────────────────────┐
│                                                              │
│                         Oooo                                 │
│                              *                               │
└────────────────────────────────────────────────────────────┘

Score: 20 | Level: 1 | Skin: classic      High Score: 280
```

### Example 2: Mid Game with Obstacles (Level 3, Blocks Skin)
```
                           SNAKE GAME
    Arrow Keys | Q: Quit | R: Restart | P: Pause | S: Skin

┌────────────────────────────────────────────────────────────┐
│                         #                                    │
│              █▓▓▓▓▓                                          │
│                ▓▓▓                                           │
│                              *                               │
│                    #                                         │
└────────────────────────────────────────────────────────────┘

Score: 110 | Level: 3 | Skin: blocks       High Score: 280
```

### Example 3: Paused Game
```
Score: 100 | Level: 3 | Skin: dots         High Score: 280
                        *** PAUSED ***
```

## Credits

These advanced features were implemented as part of Step 9 of the Snake Game improvement plan, focusing on enhancing user experience and adding replay value through progressive difficulty and customization options.

---

Enjoy the enhanced Snake Game! 🐍🎮
