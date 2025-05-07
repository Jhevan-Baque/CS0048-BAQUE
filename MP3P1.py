import os

def pause():
    input("Press Enter to continue")

def is_valid_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    
def format_result(value):
    if value == -0.0:
        value = 0.0
    if value == int(value):
        return str(int(value))
    else:
        return f"{value:.2f}"

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
            if not is_valid_number(x):
                print("Invalid Input")
                pause()
                continue
            y = input("Enter second number: ")
            if not is_valid_number(y):
                print("Invalid Input")
                pause()
                continue

            x = float(x)
            y = float(y)
            if choice == "1":
                result = int(x) + int(y)
            elif choice == "2":
                result = int(x) - int(y)
            elif choice == "3":
                result = int(x) * int(y)
            elif choice == "4":
                if y == 0:
                    print("Error: Cannot divide by zero.")
                    pause()
                    continue
                result = x / y
            print("=" * 23)
            print(f"Result: {format_result(result)}")
            print("=" * 23)
            pause()
        elif choice == "5":
            print("Thank you for using Simple Calculator!")
            break
        else:
            print("Invalid Choice!")
            pause()
            continue

SimpleCalculator()
