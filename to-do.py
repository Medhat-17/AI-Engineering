while True:
    print("\nChoose an option:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. View tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print(f"Task '{task}' added!")

    elif choice == "2":
        task = input("Enter task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print(f"Task '{task}' removed!")
        else:
            print("Task not found!")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks in your list.")
        else:
            print("Your tasks:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")
elif choice == "4":
        print("Goodbye! ")
        break

    else:
        print("Invalid choice! Try again.")
