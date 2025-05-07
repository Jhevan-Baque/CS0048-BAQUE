import os

def pause():
    input("Press Enter to continue")

def GradeCalculator():
    records = {}
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 30)
        print("{:^30}".format("Student Grade Calculator"))
        print("=" * 30)
        print("1. Add Score\n2. Calculate Average\n3. Exit")
        print("=" * 30)
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            subj = input("Enter the subject: ").upper()
            if subj == "":
                print("\nSubject name cannot be empty.")
                pause()
                continue

            if subj in records:
                print(f"\n'{subj}' already exists.")
                print("Do you want to replace the existing score? \n1: Yes\n2: No")
                yorn = input("Enter your choice: ")
                if yorn == "1":
                    pass
                elif yorn == "2":
                    continue
                else:
                    print("\nInvalid Choice!")
                    pause()
                    continue
                
            score_input = input(f"Enter the score for {subj}: ")
            try:
                score = float(score_input)
                records[subj] = score
                print(f"\nScore for {subj} added/updated.")
            except ValueError:
                print("\nInvalid score input! Please enter a numeric value.")
            pause()
        elif choice == "2":
            if not records:
                print("\nNo records available. Add scores first.")
            else:
                total = sum(records.values())
                average = total / len(records)
                print("\nSubject Scores:")
                print("-" * 30)
                for subject, score in records.items():
                    print(f"{subject:<15}: {score}")
                print("-" * 30)
                print(f"Average Grade: {average:.2f}\n")
            pause()
        elif choice == "3":
            print("\nThank you for using the Grade Calculator!")
            break
        else:
            print("\nInvalid Choice! Please select 1, 2, or 3.")
            pause()

GradeCalculator()
