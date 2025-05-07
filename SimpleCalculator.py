import os

def pause():
    input("Press Enter to continue")

def SimpleCalculator():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 23)
        print("   SIMPLE CALCULATOR")
        print("=" * 23)
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
        print("=" * 23)
        choice = input("Enter your choice (1-5): ")
        if choice in ('1', '2', '3', '4'):
            x = input("Enter first number: ")
            if not x.isnumeric():
                print("Invalid Input")
                pause()
                continue
            y = input("Enter second number: ")
            if not y.isnumeric():
                print("Invalid Input")
                pause()
                continue
            if choice == "1":
                result = int(x)+int(y)
            elif choice == "2":
                result = int(x)-int(y)
            elif choice == "3":
                result = int(x)*int(y)
            elif choice == "4":
                result = int(x)/int(y)
            print("=" * 23)
            print('Result: ' + str(result))
            print("=" * 23)
            pause()
        elif choice == "5":
            print("Thankyou for using Simple Calculator!")
            break
        else:
            print("Invalid Choice!")
            pause()
            continue

SimpleCalculator()
