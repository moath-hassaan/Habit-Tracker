import click
from habit import Habit
from database import load_habits, save_habit, initialize_db, load_habit
from analytics import filter_by_periodicity, longest_streak_all, calculate_streak

@click.group()
def cli():
    """Habit Tracker CLI"""
    initialize_db()

@cli.command()
@click.option('--name', prompt='Habit name', help='Name of the habit')
@click.option('--periodicity', prompt='Periodicity (daily/weekly)', help='Habit periodicity')
def create(name, periodicity):
    """Create a new habit."""
    habit = Habit(name=name, periodicity=periodicity)
    save_habit(habit)
    click.echo(f'Habit "{name}" created!')

@cli.command()
@click.option('--name', prompt='Habit name', help='Name of the habit to complete')
def complete(name):
    """Mark a habit as completed."""
    habits = load_habits()
    for habit in habits:
        if habit.name == name:
            habit.add_completion()
            save_habit(habit)
            click.echo(f'Habit "{name}" completed!')
            return
    click.echo(f'Habit "{name}" not found!')

@cli.command()
def list_habits():
    """List all habits."""
    habits = load_habits()
    for habit in habits:
        click.echo(f'{habit.name} ({habit.periodicity})')

@cli.command()
@click.option('--name', default=None, help='Analyze a specific habit by name (optional)')
def analyze(name):
    """Display analytics."""
    if name:
        habit = load_habit(name)
        if habit:
            click.echo(f'Habit "{habit.name}" has a streak of {calculate_streak(habit.completions, habit.periodicity)} days.')
        else:
            click.echo(f'Habit "{name}" not found!')
    else:
        habits = load_habits()
        click.echo(f'Longest streak overall: {longest_streak_all(habits)}')
        daily = filter_by_periodicity(habits, 'daily')
        click.echo(f'Daily habits: {[h.name for h in daily]}')

        
if __name__ == '__main__':
    cli()
