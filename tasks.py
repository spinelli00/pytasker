from storage import load_tasks, save_tasks

def viewtasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks registered yet.")
        return

    print("\n--- TASK LIST ---")
    for i, task in enumerate(tasks, 1):
        status = "✔️" if task.get("done") else "❌"
        print(f"{i}. {task['title']} [{status} ]")
    print()

def managetasks():
    tasks = load_tasks()
    title = input("Enter task title: ")
    new_task = {"title": title, "done": False}
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added!\n")

def removetasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to remove.\n")
        return

    viewtasks()
    try:
        index = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Removed: {removed['title']}\n")
        else:
            print("Invalid index.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def marktask():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to mark.\n")
        return

    viewtasks()
    try:
        mark = int(input("Enter the number of the task to mark as done: ")) - 1
        if 0 <= mark < len(tasks):
            tasks[mark]['done'] = True
            save_tasks(tasks)
            print(f"Task '{tasks[mark]['title']}' marked as done!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")





