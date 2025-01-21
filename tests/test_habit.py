import pytest
from datetime import datetime, timedelta
from src.habit import Habit

def test_streak_daily():
    habit = Habit("Test", "daily")
    today = datetime.now()
    habit.completions = [today - timedelta(days=i) for i in range(3)]  # 3-day streak
    assert habit.current_streak() == 3

def test_streak_weekly():
    habit = Habit("Test", "weekly")
    habit.completions = [datetime(2023, 10, i*7, 12) for i in range(1, 5)]  # 4-week streak
    assert habit.current_streak() == 4
