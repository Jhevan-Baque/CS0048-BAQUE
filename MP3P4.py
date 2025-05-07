import os, random

def pause():
    input("Press Enter to continue")

def NumberGuessing():
    attempts = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 30)
        print("{:^30}".format("NUMBER GUESSING GAME"))
        print("=" * 30)
        print("1. Play\n2. Exit")
        print("=" * 30)
        choice = input("Enter your choice (1-2): ")
        if choice == "1":
            random_int = random.randint(1, 100)
            attempts = 0
            while True:
                try:
                    guess = int(input("Guess the number (1-100): "))
                    if guess < 1 or guess > 100:
                        print("\nPlease guess a number between 1 and 100.")
                        continue
                except ValueError:
                    print("\nInvalid input! Please enter a number.\n")
                    continue

                attempts += 1

                if guess == random_int:
                    print("=" * 45)
                    print(f"   You Guessed the number in {attempts} attempt(s)!")
                    print("=" * 45)
                    pause()
                    break
                elif guess > random_int:
                    print("Too high!")
                elif guess < random_int:
                    print("Too low!")
                else:
                    attempts += 1
        elif choice == "2":
            print("\nThank you for playing the Number Guessing Game!")
            break
        else:
            print("\nInvalid choice. Please select 1 or 2.")
            pause()
            continue

NumberGuessing()
