import datetime

class Task:
    def __init__(self, description, due_date=None):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.description} (Due: {self.due_date}, Status: {status})"

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("Pending Tasks:")
            for task in self.tasks:
                print(self.tasks.index(task),task)

    def display_completed_tasks(self):
        if not self.completed_tasks:
            print("No completed tasks.")
        else:
            print("Completed Tasks:")
            for task in self.completed_tasks:
                print(task)

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks.pop(task_index)
            task.completed = True
            self.completed_tasks.append(task)
            print(f"Task '{task.description}' marked as completed.")
        else:
            print("Invalid task index.")

    def update_task(self, task_index, new_description, new_due_date):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks[task_index]
            task.description = new_description
            task.due_date = new_due_date
            print("Task updated successfully.")
        else:
            print("Invalid task index.")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task '{removed_task.description}' removed from the to-do list.")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Update Task")
        print("5. Remove Task")
        print("6. Display Completed Tasks")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional, format: YYYY-MM-DD): ")
            task = Task(description, due_date)
            todo_list.add_task(task)
            print("Task added successfully.")
        elif choice == "2":
            todo_list.display_tasks()
        elif choice == "3":
            index = int(input("Enter the index of the task to mark as completed: "))
            todo_list.mark_completed(index)
        elif choice == "4":
            index = int(input("Enter the index of the task to update: "))
            new_description = input("Enter new task description: ")
            new_due_date = input("Enter new due date (optional, format: YYYY-MM-DD): ")
            todo_list.update_task(index, new_description, new_due_date)
        elif choice == "5":
            index = int(input("Enter the index of the task to remove: "))
            todo_list.remove_task(index)
        elif choice == "6":
            todo_list.display_completed_tasks()
        elif choice == "7":
            print("Exiting the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
