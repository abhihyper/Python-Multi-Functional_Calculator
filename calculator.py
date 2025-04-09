-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
🚀 Features

1. ✅ Basic Calculator  
Performs basic math operations (+, -, *, /) between two numbers with proper error handling for division by zero.

2. 🎂 Age Calculator  
Calculates your current age from your date of birth using Python’s built-in `datetime` module.

3. 💱 USD to INR Converter  
Converts US Dollars to Indian Rupees using a fixed exchange rate (₹83.20 per $1), which you can update manually.

⚙️ Technologies Used
Python 3

Built-in datetime module

-----------------------------------------------



import datetime

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return "Cannot divide by zero" if y == 0 else x / y

def calculate_basic():
    print("\n--- Basic Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Choose operation (+, -, *, /): ")

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        else:
            result = "Invalid operation"

        print(f"Result: {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

def calculate_age():
    print("\n--- Age Calculator ---")
    dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        dob = datetime.datetime.strptime(dob_input, "%Y-%m-%d")
        today = datetime.datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        print(f"You are {age} years old.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

def usd_to_inr():
    print("\n--- Dollar to INR Converter ---")
    try:
        usd = float(input("Enter amount in USD: "))
        exchange_rate = 83.2  # You can update this as needed
        inr = usd * exchange_rate
        print(f"${usd} USD = ₹{inr:.2f} INR")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    while True:
        print("\n--- Multi Functional Calculator ---")
        print("1. Basic Calculator")
        print("2. Age Calculator")
        print("3. Dollar to INR Converter")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            calculate_basic()
        elif choice == '2':
            calculate_age()
        elif choice == '3':
            usd_to_inr()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 4.")

if __name__ == "__main__":
    main()


----------------OUTPUT-----------------------OUTPUT---------------------------OUTPUT------------------------------OUTPUT--------------------------------------------------------------------------
--- Multi Functional Calculator ---
1. Basic Calculator       
2. Age Calculator
3. Dollar to INR Converter
4. Exit
Enter your choice (1-4): 1

--- Basic Calculator ---
Enter first number: 3   
Enter second number: 6
Choose operation (+, -, *, /): -
Result: -3.0

--- Multi Functional Calculator ---
1. Basic Calculator
2. Age Calculator
3. Dollar to INR Converter
4. Exit
Enter your choice (1-4): 2

--- Age Calculator ---
Enter your date of birth (YYYY-MM-DD): 2003-04-23
You are 21 years old.

--- Multi Functional Calculator ---
1. Basic Calculator
2. Age Calculator
3. Dollar to INR Converter
Enter your choice (1-4): 3

--- Dollar to INR Converter ---
Enter amount in USD: 1
$1.0 USD = ₹83.20 INR

--- Multi Functional Calculator ---
1. Basic Calculator
2. Age Calculator
3. Dollar to INR Converter
4. Exit
Enter your choice (1-4): 4
Exiting the program. Goodbye!

---------------------------------------------------------------------------------------------------------------------------------------------------------------------
