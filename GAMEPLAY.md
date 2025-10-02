# Gameplay Guide 🎮

## Game Screen Layout

```
                           SNAKE GAME
              Use Arrow Keys | Q: Quit | R: Restart

┌────────────────────────────────────────────────────────────┐
│                                                              │
│                                                              │
│                                                              │
│                                                              │
│                         Oooo                                 │
│                                                              │
│                              *                               │
│                                                              │
│                                                              │
│                                                              │
│                                                              │
│                                                              │
└────────────────────────────────────────────────────────────┘

Score: 0                                        High Score: 0
```

## Understanding the Screen

- **Border**: The game area boundary (don't hit it!)
- **Snake Head**: `O` (capital O)
- **Snake Body**: `o` (lowercase o)
- **Food**: `*` (asterisk)
- **Score**: Displayed at bottom left
- **High Score**: Displayed at bottom right

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
| R   | Restart game |
| Q   | Quit game |

### Rules

1. **Movement**
   - Snake continuously moves in the current direction
   - Press arrow keys to change direction
   - Cannot make 180-degree turns (e.g., can't go left if moving right)

2. **Eating Food**
   - Move the snake head over the food (`*`)
   - Snake grows by one segment
   - Score increases by 10 points
   - New food appears at a random location

3. **Collision**
   - Hitting the border = Game Over
   - Hitting your own body = Game Over

4. **Game Over**
   - Score is displayed
   - Press R to restart
   - Press Q to quit
   - High score is saved for the current session

## Strategy Tips

1. **Plan Ahead**: Think about where you'll be, not just where you are
2. **Use the Center**: Stay near the center when the snake is short
3. **Avoid Corners**: Getting trapped in corners is dangerous
4. **Create Patterns**: Move in patterns to avoid tangling yourself
5. **Don't Panic**: Smooth, deliberate movements are better than frantic ones
6. **Watch Your Tail**: As you grow, your tail becomes your biggest enemy

## Scoring

- Each food eaten: **+10 points**
- No time bonus
- No penalty for length
- Goal: Achieve the highest score possible!

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

## World Records (Your Session)

Your high score is tracked during your gaming session. Try to beat it!

Challenge yourself:
- Can you reach 100 points?
- Can you reach 500 points?
- Can you fill half the screen?

---

Happy gaming! May you achieve the highest score! 🐍🏆
