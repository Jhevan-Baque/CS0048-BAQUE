import os

def pause():
    input("Press Enter to continue")

def GradeCalculator():
    records = {}
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Add Score\n2. Calculate Average\n3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            subj = input("Enter the subject: ")
            if subj in records:
                print(f"{subj}, Already Exists, Do you want to replace? \n1: Yes\n2: No")
                yorn = input("Enter your choice: ")
                if yorn == "1":
                    score = input("Enter the score: ")
                    records[str(subj)] = float(score)
                    pause()
                elif yorn == "2":
                    continue
                else:
                    print("Invalid Choice")
                    continue
            else:
                score = input("Enter the score: ")
                records[str(subj)] = float(score)
                pause()
        elif choice == "2":
            avg = 0
            for _,v in records.items():
                avg += v
            print(f"Average Grade: {avg/len(records)}")
            pause()
        elif choice == "3":
            print("Thankyou for using Grade Calculator")
            break
        else:
            print("Invalid Choice!")
            pause()
            continue

GradeCalculator()
