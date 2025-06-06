from diary import load_tasks, add_task, find_all, delete_task, toggle_task_done


def print_menu():
    print("\n===Smart Diary===")
    print("1. Add new task")
    print("2. Display all tasks")
    print("3. Delete task")
    print("4. Exit")

def main():
    tasks = load_tasks()

    while True:
        print_menu()
        choice = input("\nInput option from menu:").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            find_all(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            toggle_task_done(tasks)
        elif choice == "5":
            print("Goodbye!!!")
            break
        else:
            print("Incorrect choice. Please try again!")

if __name__ == "__main__":
    main()
