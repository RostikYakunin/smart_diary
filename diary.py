import json
import os
from datetime import datetime

STORAGE_FILE = "storage.json"
DATE_FORMAT = "%Y-%m-%d %H:%M"
ENCODING = "utf-8"


def load_tasks():
    if not os.path.exists(STORAGE_FILE):
        return []
    with open(STORAGE_FILE, "r", encoding=ENCODING) as file:
        content = file.read().strip()
        if not content:
            return []
        return json.loads(content)


def save_tasks(tasks):
    with open(STORAGE_FILE, "w", encoding=ENCODING) as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)


def generate_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def add_task(tasks):
    title = input("Input task`s name:").strip()
    date_str = input("Input date and time (example - '2025-06-10 15:30'):").strip()

    try:
        due_date = datetime.strptime(date_str, DATE_FORMAT)
    except ValueError:
        print("Wrong date`s format. Please use this format - YYYY-MM-DD HH:MM")
        return

    task = {
        "id": generate_id(tasks),
        "title": title,
        "due_date": due_date.strftime(DATE_FORMAT),
        "done": False
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Tasks was successfully added!")


def find_all(tasks):
    if not tasks:
        print("There are no tasks now!")
        return

    sorted_tasks = sorted(tasks, key=lambda t: datetime.strptime(t["due_date"], DATE_FORMAT))

    print("\n===Tasks` list===")
    for task in sorted_tasks:
        status = "✅" if task["done"] else "🕓"
        print(f"[{task['id']}] {status} {task['title']} (due {task['due_date']})")

def delete_task(tasks):
    try:
        task_id = int(input("Input task`s ID:").strip())
    except ValueError:
        print("Error: ID must be a number!")
        return

    index = next((i for i, task in enumerate(tasks) if task["id"] == task_id), None)

    if index is not None:
        deleted_task = tasks.pop(index)
        save_tasks(tasks)
        print(f"Task '{deleted_task['title']}' was deleted.")
    else:
        print(f"Task with ID {task_id} not found.")

def toggle_task_done(tasks):
    try:
        task_id = int(input("Input task`s ID for toggling status: ").strip())
    except ValueError:
        print("Error: ID must be a number!")
        return

    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]
            status = "done" if task["done"] else "not done"
            save_tasks(tasks)
            print(f"Task '{task['title']}' marked as {status}.")
            return

    print(f"Task with ID {task_id} not found.")