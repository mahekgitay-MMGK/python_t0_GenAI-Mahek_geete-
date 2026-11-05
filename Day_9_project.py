"""Mini project: a command-line study planner demonstrating Python basics."""

import json
from pathlib import Path

DATA_FILE = Path("study_tasks.json")
CATEGORIES = ("Python", "Math", "Other")  # tuple: fixed collection


class StudyPlanner:
	"""Store and manage study tasks (a simple example of a class)."""

	def __init__(self, tasks=None):
		self.tasks = tasks if tasks is not None else []  # list of dictionaries

	def add_task(self, title, category, minutes):
		task = {
			"title": title,
			"category": category,
			"minutes": minutes,
			"done": False,
		}
		self.tasks.append(task)
		print("Task added.")

	def show_tasks(self):
		if not self.tasks:
			print("No tasks yet.")
			return

		for number, task in enumerate(self.tasks, start=1):
			status = "done" if task["done"] else "not done"
			print(f"{number}. {task['title']} ({task['category']}, "
				  f"{task['minutes']} min) - {status}")

	def complete_task(self, number):
		if 1 <= number <= len(self.tasks):
			self.tasks[number - 1]["done"] = True
			print("Task marked complete.")
		else:
			print("That task number does not exist.")

	def show_summary(self):
		total_minutes = sum(task["minutes"] for task in self.tasks)
		completed = sum(task["done"] for task in self.tasks)
		# A set keeps only unique category names.
		used_categories = {task["category"] for task in self.tasks}
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


def save_tasks(planner):
	"""Write tasks to a JSON file using a context manager."""
	try:
		with DATA_FILE.open("w", encoding="utf-8") as file:
			json.dump(planner.tasks, file, indent=2)
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
		print("4. Summary  5. Exit")
		choice = input("Choose 1-5: ").strip()

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
		else:
			print("Choose a menu option from 1 to 5.")


if __name__ == "__main__":
	main()
