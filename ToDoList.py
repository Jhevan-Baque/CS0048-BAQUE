import os

def pause():
    input("Press Enter to continue")

def TodoList():
    tasks = []

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Add Task\n2. Remove Task\n3. View Task\n4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            addt = input("Enter the task to add: ")
            tasks.append(addt)
            print("Task Added!")
            pause()
        elif choice == "2":
            removet = input("Enter the task id to remove task: ")
            try: 
                del tasks[(int(removet)-1)]
                pause()
            except:
                print("An Error Occured!")
                pause()
        elif choice == "3":
            print("[ Tasks ]")
            counter = 1
            for task in tasks:
                print(f"[ID: {counter}] {task}")
                counter += 1
            pause()
        elif choice == "4":
            print("Thankyou for using Simple To Do List!")
            break
        else:
            print("Invalid Choice!")
            pause()
            continue

TodoList()
