from datetime import datetime
from typing import List

class Habit:
    def __init__(self, name: str, periodicity: str, creation_date: datetime = datetime.now()):
        self.name = name
        self.periodicity = periodicity  # "daily" or "weekly"
        self.creation_date = creation_date
        self.completions: List[datetime] = []

    def add_completion(self, completion_time: datetime = datetime.now()):
        """Mark the habit as completed at a specific time."""
        self.completions.append(completion_time)
        self.completions.sort()  # Ensure chronological order

    def current_streak(self) -> int:
        """Calculate the current streak using functional programming."""
        from analytics import calculate_streak
        return calculate_streak(self.completions, self.periodicity)
