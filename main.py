class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        task_id = len(self.tasks) + 1
        self.tasks[task_id] = {"task": task, "completed": False}
        print(f"Task '{task}' added with ID {task_id}.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        print("\n--- Task List ---")
        for task_id, task_info in self.tasks.items():
            status = "Completed" if task_info["completed"] else "Pending"
            print(f"{task_id}. {task_info['task']} [{status}]")

    def complete_task(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id]["completed"] = True
            print(f"Task {task_id} marked as completed.")
        else:
            print(f"Task with ID {task_id} not found.")

    def remove_task(self, task_id):
        if task_id in self.tasks:
            removed_task = self.tasks.pop(task_id)
            print(f"Task '{removed_task['task']}' removed.")
        else:
            print(f"Task with ID {task_id} not found.")


def main():
    todo_list = ToDoList()

    while True:
        print("\n--- Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter the new task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_id = int(input("Enter the ID of the task to mark as completed: "))
            todo_list.complete_task(task_id)
        elif choice == "4":
            task_id = int(input("Enter the ID of the task to remove: "))
            todo_list.remove_task(task_id)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()