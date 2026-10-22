# Project 01: Interactive Calculator & Unit Converter
# Features: basic arithmetic, unit conversion, input validation and while loops.

def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculator():
    while True:
        print("\n--- Basic Calculator ---")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Back to main menu")
        choice = input("Choose an operation: ").strip()

        if choice == "5":
            return
        if choice not in {"1", "2", "3", "4"}:
            print("Please choose an option from 1 to 5.")
            continue

        first = get_number("Enter first number: ")
        second = get_number("Enter second number: ")

        if choice == "1":
            result = first + second
        elif choice == "2":
            result = first - second
        elif choice == "3":
            result = first * second
        else:
            if second == 0:
                print("Division by zero is not allowed. Try again.")
                continue
            result = first / second

        print(f"Result: {result:g}")


def unit_converter():
    while True:
        print("\n--- Unit Converter ---")
        print("1. Kilometres to miles")
        print("2. Miles to kilometres")
        print("3. Celsius to Fahrenheit")
        print("4. Fahrenheit to Celsius")
        print("5. Back to main menu")
        choice = input("Choose a conversion: ").strip()

        if choice == "5":
            return
        if choice not in {"1", "2", "3", "4"}:
            print("Please choose an option from 1 to 5.")
            continue

        value = get_number("Enter value to convert: ")
        if choice == "1":
            result, unit = value * 0.621371, "miles"
        elif choice == "2":
            result, unit = value / 0.621371, "kilometres"
        elif choice == "3":
            result, unit = (value * 9 / 5) + 32, "°F"
        else:
            result, unit = (value - 32) * 5 / 9, "°C"

        print(f"Converted value: {result:.2f} {unit}")


def main():
    while True:
        print("\n===== Interactive Calculator & Unit Converter =====")
        print("1. Calculator")
        print("2. Unit converter")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            calculator()
        elif choice == "2":
            unit_converter()
        elif choice == "3":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice. Enter 1, 2 or 3.")


if __name__ == "__main__":
    main()
