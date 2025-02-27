from typing import List, Optional
from datetime import datetime, timedelta
from habit import Habit

def filter_by_periodicity(habits: List[Habit], periodicity: str) -> List[Habit]:
    """Filter habits by periodicity."""
    return list(filter(lambda h: h.periodicity == periodicity, habits))

def calculate_streak(completions: List[datetime], periodicity: str) -> int:
    """Calculate the longest streak for a habit's completions."""
    if not completions:
        return 0
    # Group completions into periods (day/week)
    periods = sorted({comp.date() if periodicity == "daily" else comp.isocalendar()[:2] for comp in completions})
    max_streak = current_streak = 1
    for i in range(1, len(periods)):
        if (periods[i] - periods[i-1]) == (1 if periodicity == "daily" else (0, 1)):
            current_streak += 1
        else:
            max_streak = max(max_streak, current_streak)
            current_streak = 1
    return max(max_streak, current_streak)


def longest_streak_all(habits: List[Habit]) -> int:
    """Longest streak across all habits."""
    streaks = [calculate_streak(h.completions, h.periodicity) for h in habits]
    return max(streaks) if streaks else 0

def longest_streak_habit(habit: Habit) -> int:
    """Longest streak for a specific habit."""
    return calculate_streak(habit.completions, habit.periodicity)
