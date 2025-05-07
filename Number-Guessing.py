import os, random

def pause():
    input("Press Enter to continue")

def NumberGuessing():
    attempts = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 26)
        print("   NUMBER GUESSING GAME")
        print("=" * 26)
        print("1. Play\n2. Exit")
        choice = input("Enter your choice (1-2): ")
        if choice == "1":
            random_int = random.randint(1, 100)
            while True:
                guess = input("Guess the number (1-100): ")
                if int(guess) == random_int:
                    attempts += 1
                    print("=" * 45)
                    print(f"   You Guessed the number in {attempts} attempt(s).")
                    print("=" * 45)
                    pause()
                    break
                elif int(guess) > random_int:
                    attempts += 1
                    print("Too high!")
                elif int(guess) < random_int:
                    attempts += 1
                    print("Too low!")
                else:
                    attempts += 1
        elif choice == "2":
            print("Thankyou for using Number Guessing Game!")
            break
        else:
            print("Invalid Choice!")
            pause()
            continue

NumberGuessing()
