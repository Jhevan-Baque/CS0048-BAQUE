import os

def pause():
    input("Press Enter to continue")

def NumberGuessing():
    numofsubj = 0
    avg = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Add Score\n2. Calculate Average\n3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            subj = input("Enter the subject: ")
            numofsubj += 1
            score = input("Enter the score: ")
            avg += float(score)
            pause()
        elif choice == "2":
            print(f"Average Grade: {float(avg/numofsubj)}")
            pause()
        elif choice == "3":
            print("Thankyou for using Grade Calculator")
            pause()
        else:
            print("Invalid Choice!")
            pause()
            continue

NumberGuessing()
