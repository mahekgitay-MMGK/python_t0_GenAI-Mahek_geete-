"""Mini project: a command-line study planner demonstrating Python basics.

Project guide
=============
This command-line program helps a learner track study tasks. The menu can add
tasks, display all tasks, mark a task complete, show totals, and filter tasks
by category. Tasks are stored in ``study_tasks.json`` in the current working
directory, so valid tasks persist between runs.

Main parts
----------
* ``StudyTask`` is a dataclass containing a title, category, study time in
	minutes, and completion status. ``from_dict`` validates data read from JSON.
* ``StudyPlanner`` manages the task list. Its methods add tasks, lazily iterate
	over tasks (optionally filtered), print tasks, complete a numbered task, and
	calculate a summary. Task numbers start at 1 for the user.
* ``load_tasks`` reads JSON and handles missing, unreadable, or malformed
	files. Invalid individual task records are skipped by the planner.
	``save_tasks`` converts dataclasses to dictionaries and writes formatted
	JSON.
* ``get_positive_integer`` keeps asking until the user enters a whole number
	greater than zero. The menu loop uses ``if``/``elif`` branches to run the
	selected action.
* ``CATEGORIES`` is a tuple of supported categories. Input is normalized with
	``title()``; an unrecognized category is assigned to ``Other``.

Example output
==============
For a fresh save file, adding a task and displaying the list and summary
produces output like this. Text after prompts is sample user input::

		=== My Study Planner ===
		1. Add task  2. Show tasks  3. Complete task
		4. Summary  5. Exit  6. Filter by category
		Choose 1-6: 1
		Task title: Review Python
		Categories: Python, Math, Other
		Category: Python
		Study minutes: 30
		Task added.
		Choose 1-6: 2
		1. Review Python (Python, 30 min) - not done
		Choose 1-6: 4
		Tasks: 1 | Completed: 0 | Study time: 30 minutes
		Categories used: Python

The menu is printed again after each action. Selecting 3 asks for a task
number and marks that task complete; selecting 5 saves and exits. Exact output
depends on the user's input and tasks already saved.
"""

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterator

DATA_FILE = Path("study_tasks.json")
CATEGORIES = ("Python", "Math", "Other")  # tuple: fixed collection


@dataclass
class StudyTask:
	"""A typed task record; dataclasses provide generated init/repr methods."""

	title: str
	category: str
	minutes: int
	done: bool = False

	@classmethod
	def from_dict(cls, data: dict) -> "StudyTask":
		"""Build a task from saved JSON and reject malformed records."""
		title = data.get("title")
		category = data.get("category")
		minutes = data.get("minutes")
		done = data.get("done", False)
		if (not isinstance(title, str) or not isinstance(category, str)
				or not isinstance(minutes, int) or isinstance(minutes, bool) or minutes <= 0
				or not isinstance(done, bool)):
			raise ValueError("Invalid task data")
		return cls(title, category, minutes, done)


class StudyPlanner:
	"""Store and manage study tasks (a simple example of a class)."""

	def __init__(self, tasks: list[dict] | None = None):
		self.tasks: list[StudyTask] = []
		for data in tasks or []:
			try:
				self.tasks.append(StudyTask.from_dict(data))
			except (AttributeError, ValueError):
				print("Skipped an invalid saved task.")

	def add_task(self, title: str, category: str, minutes: int) -> None:
		self.tasks.append(StudyTask(title, category, minutes))
		print("Task added.")

	def iter_tasks(self, category: str | None = None) -> Iterator[tuple[int, StudyTask]]:
		"""Yield matching tasks lazily, preserving their original task numbers."""
		return ((number, task) for number, task in enumerate(self.tasks, start=1)
				if category is None or task.category == category)

	def show_tasks(self, category: str | None = None) -> None:
		tasks = list(self.iter_tasks(category))
		if not tasks:
			print("No tasks yet.")
			return

		for number, task in tasks:
			status = "done" if task.done else "not done"
			print(f"{number}. {task.title} ({task.category}, "
				  f"{task.minutes} min) - {status}")

	def complete_task(self, number: int) -> None:
		if 1 <= number <= len(self.tasks):
			self.tasks[number - 1].done = True
			print("Task marked complete.")
		else:
			print("That task number does not exist.")

	def show_summary(self) -> None:
		total_minutes = sum(task.minutes for task in self.tasks)
		completed = sum(task.done for task in self.tasks)
		# A set keeps only unique category names.
		used_categories = {task.category for task in self.tasks}
		print(f"Tasks: {len(self.tasks)} | Completed: {completed} | "
			  f"Study time: {total_minutes} minutes")
		print("Categories used:", ", ".join(sorted(used_categories)) or "none")


def load_tasks():
	"""Read saved JSON data; use an empty list if no save exists yet."""
	try:
		with DATA_FILE.open("r", encoding="utf-8") as file:
			data = json.load(file)
			return data if isinstance(data, list) else []
	except FileNotFoundError:
		return []
	except (json.JSONDecodeError, OSError) as error:
		print(f"Could not load saved tasks: {error}")
		return []



def save_tasks(planner: StudyPlanner) -> None:
	"""Write tasks to a JSON file using a context manager."""
	try:
		with DATA_FILE.open("w", encoding="utf-8") as file:
			json.dump([asdict(task) for task in planner.tasks], file, indent=2)
	except OSError as error:
		print(f"Could not save tasks: {error}")


def get_positive_integer(message):
	"""Convert input text to an integer and validate it."""
	while True:
		try:
			value = int(input(message))  # input gives a string; convert its type
			if value > 0:
				return value
			print("Enter a number greater than zero.")
		except ValueError:
			print("Please enter a whole number.")


def main():
	planner = StudyPlanner(load_tasks())
	print("\n=== My Study Planner ===")

	# while loop repeats the menu; if/elif/else selects an action.
	while True:
		print("\n1. Add task  2. Show tasks  3. Complete task")
		print("4. Summary  5. Exit  6. Filter by category")
		choice = input("Choose 1-6: ").strip()

		if choice == "1":
			title = input("Task title: ").strip()
			if not title:
				print("A title cannot be empty.")
				continue  # skip to the next menu iteration
			print("Categories:", ", ".join(CATEGORIES))
			category = input("Category: ").strip().title()
			if category not in CATEGORIES:
				category = "Other"
			minutes = get_positive_integer("Study minutes: ")
			planner.add_task(title, category, minutes)
			save_tasks(planner)
		elif choice == "2":
			planner.show_tasks()
		elif choice == "3":
			planner.show_tasks()
			if planner.tasks:
				number = get_positive_integer("Task number to complete: ")
				planner.complete_task(number)
				save_tasks(planner)
		elif choice == "4":
			planner.show_summary()
		elif choice == "5":
			save_tasks(planner)
			print("Tasks saved. Happy studying!")
			break
		elif choice == "6":
			print("Categories:", ", ".join(CATEGORIES))
			category = input("Category: ").strip().title()
			planner.show_tasks(category if category in CATEGORIES else "Other")
		else:
			print("Choose a menu option from 1 to 6.")


if __name__ == "__main__":
	main()
