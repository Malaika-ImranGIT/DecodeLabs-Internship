def add_task(task_list, new_task):
    task = new_task.strip()
    if not task:
        return False
    task_list.append(task)
    return True

def display_tasks(task_list):
    print("\n--- TO-DO LIST ---")
    if not task_list:
        print("No tasks found.")
    else:
        for index, task in enumerate(task_list, start=1):
            print(f"[{index}] {task}")

def run_todo_engine():
    my_tasks = []
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Exit")
        choice = input("Select an option: ").strip()
        if choice == '1':
            new_task = input("Enter new task: ")
            if add_task(my_tasks, new_task):
                print("Task added.")
            else:
                print("Invalid input.")
        elif choice == '2':
            display_tasks(my_tasks)
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    run_todo_engine()