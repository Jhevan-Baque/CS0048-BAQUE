import os

def pause():
    input("\nPress Enter to continue")

def TodoList():
    tasks = []

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 30)
        print("{:^30}".format("To-Do List Manager"))
        print("=" * 30)
        print("1. Add Task\n2. Remove Task\n3. View Task\n4. Exit")
        print("=" * 30)

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            addt = input("\nEnter the task to add: ")
            if addt:
                tasks.append(addt)
                print("\nTask added successfully.")
            else:
                print("\nTask cannot be empty!")
            pause()
        elif choice == "2":
            if len(tasks) == 0:
                print("\nNo tasks available to remove.")
                pause()
                continue
            removet = input("\nEnter the task ID to remove task: ")
            try: 
                del tasks[(int(removet)-1)]
                print("\nTask Removed!")
                pause()
            except:
                print("\nAn Error Occurred! Please enter a valid task ID.")
                pause()
        elif choice == "3":
            if len(tasks) == 0:
                print("\nNo tasks to display.")
            else:
                print("\n" + "=" * 30)
                print("{:<5} {:<20}".format("ID", "Task"))
                print("=" * 30)
                counter = 1
                for task in tasks:
                    print("{:<5} {:<20}".format(counter, task))
                    counter += 1
            pause()
        elif choice == "4":
            print("\nThank you for using Simple To-Do List!")
            break
        else:
            print("\nInvalid Choice! Please choose 1, 2, 3, or 4.")
            pause()
            continue

TodoList()
