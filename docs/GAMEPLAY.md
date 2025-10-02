# Gameplay Guide 🎮

## Game Screen Layout

```
                           SNAKE GAME
    Arrow Keys | Q: Quit | R: Restart | P: Pause | S: Skin

┌────────────────────────────────────────────────────────────┐
│                                                              │
│                         #                                    │
│                                                              │
│                                                              │
│                         Oooo                                 │
│                                                              │
│                              *                               │
│                                                              │
│                    #                                         │
│                                                              │
│                                                              │
│                                                              │
└────────────────────────────────────────────────────────────┘

Score: 40 | Level: 2 | Skin: classic      High Score: 120
```

## Understanding the Screen

- **Border**: The game area boundary (don't hit it!)
- **Snake Head**: `O` (varies with skin)
- **Snake Body**: `o` (varies with skin)
- **Food**: `*` (asterisk)
- **Obstacles**: `#` (appear at level 3+)
- **Score**: Displayed at bottom left
- **Level**: Current difficulty level
- **Skin**: Current snake appearance
- **High Score**: All-time high score (persisted)

## Gameplay Mechanics

### Starting the Game

When you start the game:
1. Snake appears in the center with 3 segments
2. Food appears randomly on the screen
3. Snake starts moving to the right
4. Score is 0

### Controls

| Key | Action |
|-----|--------|
| ↑   | Move up |
| ↓   | Move down |
| ←   | Move left |
| →   | Move right |
| P   | Pause/Resume game |
| S   | Change snake skin |
| L   | View leaderboard |
| R   | Restart game |
| Q   | Quit game |

**Pro Tip**: Use the pause feature (P key) to take a break without losing your progress!

### Rules

1. **Movement**
   - Snake continuously moves in the current direction
   - Press arrow keys to change direction
   - Cannot make 180-degree turns (e.g., can't go left if moving right)
   - Use P to pause at any time

2. **Eating Food**
   - Move the snake head over the food (`*`)
   - Snake grows by one segment
   - Score increases by 10 points
   - New food appears at a random location

3. **Level Progression**
   - Start at Level 1
   - Every 50 points advances you to the next level
   - Game speed increases with each level
   - Obstacles (`#`) appear starting at Level 3
   - Each level adds 2 more obstacles

4. **Collision**
   - Hitting the border = Game Over
   - Hitting your own body = Game Over
   - Hitting an obstacle = Game Over

5. **Game Over**
   - Final score and level are displayed
   - Score is automatically saved to leaderboard
   - Press L to view leaderboard
   - Press R to restart
   - Press Q to quit
   - High score persists across sessions

## Snake Skins

Choose from 4 different visual styles by pressing 'S':

1. **Classic** - Traditional snake appearance
   - Head: `O`  Body: `o`

2. **Blocks** - Solid block style
   - Head: `█`  Body: `▓`

3. **Arrows** - Directional arrow style
   - Head: `>`  Body: `-`

4. **Dots** - Circular dot style
   - Head: `●`  Body: `○`

## Strategy Tips

1. **Plan Ahead**: Think about where you'll be, not just where you are
2. **Use the Center**: Stay near the center when the snake is short
3. **Avoid Corners**: Getting trapped in corners is dangerous
4. **Create Patterns**: Move in patterns to avoid tangling yourself
5. **Don't Panic**: Smooth, deliberate movements are better than frantic ones
6. **Watch Your Tail**: As you grow, your tail becomes your biggest enemy
7. **Navigate Obstacles**: Plan your route around obstacles at higher levels
8. **Use Pause**: Press P to pause and plan your next moves
9. **Speed Management**: Be prepared for faster gameplay at higher levels
10. **Leaderboard Goals**: Check the leaderboard (L) to see what score to beat

## Scoring

- Each food eaten: **+10 points**
- Level advancement: Every **50 points**
- No time bonus
- No penalty for length
- Goal: Achieve the highest score possible and make it to the leaderboard!

## Leaderboard

- Top 10 scores are saved permanently
- Each entry shows:
  - Rank (1-10)
  - Score
  - Level reached
  - Date and time achieved
- Access leaderboard:
  - During game: Press L
  - After game over: Press L
- Challenge yourself to reach the top!

## Example Game Progression

### Beginning (Score: 0)
```
┌──────────────┐
│              │
│    Ooo       │
│              │
│       *      │
└──────────────┘
```

### Mid-Game (Score: 50)
```
┌──────────────┐
│              │
│    Oooooo    │
│      ooo     │
│   *          │
└──────────────┘
```

### Advanced (Score: 150)
```
┌──────────────┐
│   ooOoooo    │
│   ooooooo    │
│   ooo  ooo   │
│   *    ooo   │
└──────────────┘
```

## Terminal Requirements

For the best experience:
- **Minimum Size**: 80 columns × 24 rows
- **Recommended**: 100 columns × 30 rows or larger
- **Terminal**: Any modern terminal with curses support
- **Colors**: Not required (game uses ASCII characters)

## Common Issues

**Q: The snake is too fast!**
A: The game speed is fixed at 100ms refresh. This is normal for Snake games.

**Q: The snake is too slow!**
A: Your terminal might be lagging. Try a lighter terminal emulator.

**Q: I can't see the border clearly**
A: Resize your terminal window or use a terminal with better character rendering.

**Q: Keys are not responding**
A: Make sure the terminal window has focus and you're pressing arrow keys (not WASD).

## Game Over Screen

When you lose:
```
┌────────────────────────────────────────────────────────────┐
│                                                              │
│                                                              │
│                                                              │
│                                                              │
│                        GAME OVER!                            │
│                     Final Score: 120                         │
│                                                              │
│               Press R to restart or Q to quit                │
│                                                              │
│                                                              │
│                                                              │
│                                                              │
└────────────────────────────────────────────────────────────┘
```

## High Score Tracking

Your high score is automatically saved and persists across gaming sessions!

The high score is stored in: `~/.snake_game_high_score.json`

Challenge yourself:
- Can you reach 100 points?
- Can you reach 500 points?
- Can you fill half the screen?
- Can you beat your personal best?

---

Happy gaming! May you achieve the highest score! 🐍🏆
