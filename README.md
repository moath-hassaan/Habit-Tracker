# Habit Tracker

A Python-based command-line application for building and maintaining habits. The app tracks habit completion, provides insightful analytics, and stores data persistently using SQLite.

## Features
- **Create Habits:** Define habits with names and periodicity (daily, weekly, etc.).
- **Completion Tracking:** Mark habits as completed.
- **Habit List:** View all active habits.
- **Analytics:** Track streaks, completion rates, and identify patterns.
- **Data Persistence:** Store habit data in an SQLite database.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/habit-tracker.git
   cd habit-tracker
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Seed Sample Data (Optional):**
   ```bash
   python seed.py
   ```

## Usage

Run the CLI:
```bash
python -m cli [COMMAND]
```

### Commands:
- `create` — Create a new habit.
- `complete` — Mark a habit as complete.
- `list_habits` — Show all habits.
- `analyze` — View habit analytics.

Example:
```bash
python -m cli create "Morning Workout" daily
python -m cli complete "Morning Workout"
python -m cli analyze
```

## Project Structure
```
├── cli.py          # Command-line interface
├── habit.py        # Habit model definition
├── database.py     # Database interactions (SQLite)
├── analytics.py    # Habit analysis and insights
├── seed.py         # Seed script for test data
├── tests/          # Unit tests
└── habits.db       # SQLite database file
```


