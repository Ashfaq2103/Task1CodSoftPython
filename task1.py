class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        print(f"Added: {task}")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Removed: {removed_task['task']}")
        else:
            print("Invalid task number.")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
            print(f"Task '{self.tasks[index]['task']}' marked as completed.")
        else:
            print("Invalid task number.")

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            for i, task in enumerate(self.tasks, 1):
                status = "Completed" if task['completed'] else "Not Completed"
                print(f"{i}. {task['task']} - {status}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input("Enter task number to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == '3':
            index = int(input("Enter task number to mark as completed: ")) - 1
            todo_list.mark_completed(index)
        elif choice == '4':
            todo_list.view_tasks()
        elif choice == '5':
            print("Exiting the to-do list.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
