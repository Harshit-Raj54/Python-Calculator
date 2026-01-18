def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero!"

def power(a, b):
    return a ** b

def calculator():
    print("Welcome to Python Calculator")
    print("Operations: +, -, x, ÷, ** (power)")
    
    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operation (+, -, x, ÷, **): ").strip()
            num2 = float(input("Enter second number: "))
            
            if op == "+":
                result = add(num1, num2)
            elif op == "-":
                result = subtract(num1, num2)
            elif op.lower() == "x":
                result = multiply(num1, num2)
            elif op == "÷":
                result = divide(num1, num2)
            elif op == "**":
                result = power(num1, num2)
            else:
                print("Invalid operation! Try again.")
                continue

            print(f"Result: {result}")

        except ValueError:
            print("Invalid input! Please enter numbers only.")
        
        # Ask if user wants to continue
        again = input("Do you want to continue? (y/n): ").strip().lower()
        if again != "y":
            print("Thank you for using Python Calculator!")
            break

if __name__ == "__main__":
    calculator()