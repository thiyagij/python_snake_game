"""
Score Manager Module
Handles loading and saving high scores.
"""

import json
import os


class ScoreManager:
    """Manages high score persistence."""

    def __init__(self, score_file):
        """Initialize score manager with file path."""
        self.score_file = score_file

    def load_high_score(self):
        """Load high score from file."""
        try:
            if os.path.exists(self.score_file):
                with open(self.score_file, 'r') as f:
                    data = json.load(f)
                    return data.get('high_score', 0)
        except Exception:
            pass
        return 0

    def save_high_score(self, score):
        """Save high score to file."""
        try:
            with open(self.score_file, 'w') as f:
                json.dump({'high_score': score}, f)
        except Exception:
            pass
