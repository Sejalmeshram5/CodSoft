tasks = []
next_id = 1

def add_task(task_description):
    global next_id
    task = {
        'id': next_id,
        'task': task_description,
        'status': 'Pending'
    }
    tasks.append(task)
    next_id += 1
    print(f"Task '{task_description}' added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks to show.")
    else:
        for task in tasks:
            print(f"{task['id']}: {task['task']} [{task['status']}]")

def mark_task_completed(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'Completed'
            print(f"Task '{task['task']}' marked as completed!")
            return
    print("Task not found.")

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    print("Task deleted if it existed.")

def update_task(task_id, new_description):
    for task in tasks:
        if task['id'] == task_id:
            task['task'] = new_description
            print(f"Task ID {task_id} updated successfully!")
            return
    print("Task not found.")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Update Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task_description = input("Enter the task description: ")
            add_task(task_description)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_id = int(input("Enter the task ID to mark as completed: "))
            mark_task_completed(task_id)
        elif choice == '4':
            task_id = int(input("Enter the task ID to delete: "))
            delete_task(task_id)
        elif choice == '5':
            task_id = int(input("Enter the task ID to update: "))
            new_description = input("Enter the new task description: ")
            update_task(task_id, new_description)
        elif choice == '6':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
