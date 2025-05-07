import os

def pause():
    input("Press Enter to continue")

def TemperatureConverter():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Convert Celsius to Fahrenheit\n2. Convert Fahrenheit to Celsius\n3. Exit")

        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            cel = input("Enter temperature in Celsius: ")
            if not cel.isnumeric():
                print("Invalid Input: Try a Integer")
                pause()
                continue
            print(f"Temperature in Fahrenheit: {float((float(cel) * 1.8) + 32)}")
            pause()
        elif choice == "2":
            fah = input("Enter temperature in Fahrenheit: ")
            if not fah.isnumeric():
                print("Invalid Input: Try a Integer")
                pause()
                continue
            print(f"Temperature in Celsius: {float((float(fah) - 32) / 1.8)}")
            pause()
        elif choice == "3":
            print("Thankyou for using Simple Calculator!")
            break
        else:
            print("Invalid Choice!")
            pause()
            continue

TemperatureConverter()
