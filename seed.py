from datetime import datetime, timedelta
from database import save_habit
from habit import Habit

def seed_data():
    # Create sample habits
    habits = [
        Habit("Exercise", "daily"),
        Habit("Read", "daily"),
        Habit("Meditate", "weekly"),
        Habit("Drink Water", "daily"),
        Habit("Weekly Review", "weekly"),
    ]
    # Add 4 weeks of completions
    today = datetime.now()
    for habit in habits:
        for days_ago in range(28):  # 4 weeks
            date = today - timedelta(days=days_ago)
            if habit.periodicity == "daily" or (days_ago % 7 == 0):
                habit.add_completion(date)
        save_habit(habit)

if __name__ == '__main__':
    seed_data()
