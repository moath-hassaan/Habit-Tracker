import sqlite3
from datetime import datetime
from typing import List
from habit import Habit

def initialize_db():
    """Create tables for habits and completions."""
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE,
            periodicity TEXT,
            creation_date TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS completions (
            id INTEGER PRIMARY KEY,
            habit_id INTEGER,
            completion_date TEXT,
            FOREIGN KEY(habit_id) REFERENCES habits(id)
        )
    ''')
    conn.commit()
    conn.close()

def save_habit(habit: Habit):
    """Save a habit and its completions to the database."""
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    # Insert or replace habit
    c.execute('''
        INSERT OR REPLACE INTO habits (name, periodicity, creation_date)
        VALUES (?, ?, ?)
    ''', (habit.name, habit.periodicity, habit.creation_date.isoformat()))
    # Insert completions
    habit_id = c.lastrowid
    for comp in habit.completions:
        c.execute('''
            INSERT INTO completions (habit_id, completion_date)
            VALUES (?, ?)
        ''', (habit_id, comp.isoformat()))
    conn.commit()
    conn.close()

def load_habits() -> List[Habit]:
    """Load all habits and their completions from the database."""
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    habits = []
    c.execute('SELECT id, name, periodicity, creation_date FROM habits')
    for row in c.fetchall():
        habit = Habit(
            name=row[1],
            periodicity=row[2],
            creation_date=datetime.fromisoformat(row[3])
        )
        c.execute('''
            SELECT completion_date FROM completions
            WHERE habit_id = ?
        ''', (row[0],))
        completions = [datetime.fromisoformat(comp[0]) for comp in c.fetchall()]
        habit.completions = completions
        habits.append(habit)
    conn.close()
    return habits

def load_habit(name: str) -> Habit | None:
    """Load a single habit by name from the database."""
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    
    c.execute('SELECT id, name, periodicity, creation_date FROM habits WHERE name = ?', (name,))
    row = c.fetchone()
    
    if row is None:
        conn.close()
        return None  # Return None if no habit is found
    
    habit = Habit(
        name=row[1],
        periodicity=row[2],
        creation_date=datetime.fromisoformat(row[3])
    )
    
    c.execute('SELECT completion_date FROM completions WHERE habit_id = ?', (row[0],))
    completions = [datetime.fromisoformat(comp[0]) for comp in c.fetchall()]
    habit.completions = completions
    
    conn.close()
    return habit
    