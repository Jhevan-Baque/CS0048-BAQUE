import os

def pause():
    input("Press Enter to continue")

def is_valid_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def TemperatureConverter():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 35)
        print("{:^35}".format("  Temperature Converter  "))
        print("=" * 35)
        print("1. Convert Celsius to Fahrenheit\n2. Convert Fahrenheit to Celsius\n3. Exit")
        print("=" * 35)

        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            cel = input("Enter temperature in Celsius: ")
            if not is_valid_number(cel):
                print("\nInvalid Input! Please enter a valid number.")
                pause()
                continue
            result = (float(cel) * 1.8) + 32
            print(f"\nTemperature in Fahrenheit: {result:.2f} °F")
            pause()
        elif choice == "2":
            fah = input("Enter temperature in Fahrenheit: ")
            if not is_valid_number(fah):
                print("\nInvalid Input! Please enter a valid number.")
                pause()
                continue
            result = (float(fah) - 32) / 1.8
            print(f"\nTemperature in Celsius: {result:.2f} °C")
            pause()
        elif choice == "3":
            print("Thankyou for using Temperature Converter!")
            break
        else:
            print("\nInvalid Choice! Please choose 1, 2, or 3.")
            pause()
            continue

TemperatureConverter()
