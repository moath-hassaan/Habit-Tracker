# Habit-Tracker



# Habit Tracker

A Python-based habit tracking application with CLI, analytics, and SQLite persistence.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/habit-tracker.git
   cd habit-tracker


   Install dependencies:

bash
Copy
pip install -r requirements.txt
Seed sample data:

bash
Copy
python -m src.seed




python -m src.cli [COMMAND]

Commands:
  create     Create a new habit
  complete   Mark a habit as completed
  list_habits  List all habits
  analyze    Display analytics



  
---

### **Implementation Notes**
- **Modularity**: Components are separated into `habit`, `database`, `analytics`, and `cli`.
- **Functional Programming**: Analytics use `filter`, `map`, and list comprehensions.
- **Error Handling**: Input validation in CLI commands (e.g., periodicity checks).
- **Extensibility**: Easy to add new features like GUI or web interfaces.

Run the CLI with `python -m src.cli` and follow the prompts!
