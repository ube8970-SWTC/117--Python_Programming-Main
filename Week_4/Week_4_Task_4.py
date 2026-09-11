
class ClassTracker:
	def __init__(self):
		self.classes = {}

# able to add a new class and have multiple classes.
	def add_class(self, name):
		if name not in self.classes:
			self.classes[name] = []

# able to add a new tasks and each class can have multiple tasks.
	def add_task(self, class_name, task):
		self.add_class(class_name)
		self.classes[class_name].append({"task": task, "done": False})

	def complete_task(self, class_name, task_number):
		tasks = self.classes.get(class_name, [])
		if 1 <= task_number <= len(tasks):
			tasks[task_number - 1]["done"] = True
			return True
		return False

	def display(self):
		if not self.classes:
			print("No classes or tasks yet.")
			return

		for class_name, tasks in self.classes.items():
			print(f"\n{class_name}")
			if not tasks:
				print("  No tasks")
			for number, item in enumerate(tasks, 1):
				status = "x" if item["done"] else " "
				print(f"  [{status}] {number}. {item['task']}")

# main menu type of interface that allows the user to choose what they want to do.
# feels weird to write user or individual but it makes more sense than person or student.

def main():
	tracker = ClassTracker()

	while True:
		print("\n1. Add class\n2. Add task\n3. Complete task\n4. View tracker\n5. Quit")
		choice = input("Choose an option: ").strip()

		if choice == "1":
			tracker.add_class(input("Class name: ").strip())
		elif choice == "2":
			class_name = input("Class name: ").strip()
			task = input("Task: ").strip()
			tracker.add_task(class_name, task)
		elif choice == "3":
			class_name = input("Class name: ").strip()
			try:
				task_number = int(input("Task number: "))
				if not tracker.complete_task(class_name, task_number):
					print("Task not found.")
			except ValueError:
				print("Enter a valid task number.")
		elif choice == "4":
			tracker.display()
		elif choice == "5":
			print("Goodbye!")
			break
		else:
			print("Invalid option.")


if __name__ == "__main__":
	main()
