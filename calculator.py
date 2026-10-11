#-----------------------------------CALCULATOR IN PYTHON-----------------------------------#

def add(a:float,b:float)-> float:
    """
    This function takes two numbers as input and returns their sum.
    """
    return a + b


def subtract(a:float,b:float)-> float:
    """
    This function takes two numbers as input and returns their difference.
    """
    return a - b



def multiply(a:float,b:float)-> float:
    """
    This function takes two numbers as input and returns their product.
    """
    return a * b
# product = multiply(10, 5)
# print(f"The product is: {product}")

def divide(a:float,b:float)-> float:
    """
    This function takes two numbers as input and returns their quotient.
    """
    if b == 0:
        raise ValueError("Error: Division by zero is not allowed.")
        
    
    return a / b
# quotient = divide(10, 5)
# print(f"The quotient is: {quotient}")

print("\n==================================")
print("       PYTHON CALCULATOR")
print("==================================\n")

print("\n----------------------------------------------")
print("  select an operation to perform:")
print("----------------------------------------------\n")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("----------------------------------------------")
choice = (input("\nEnter your choice (1-4) or Select Operation: "))

def perform_operation(choice):
    match choice:
        case "addition" | "1":
            a,b = float(input("Enter first number: ")), float(input("Enter second number: "))
            total = add(a, b)
            print(f"The sum is: {total}")
    
        case "subtraction" | "2":
            a,b = float(input("Enter first number: ")), float(input("Enter second number: "))
            difference = subtract(a, b)
            print(f"The difference is: {difference}")

        case "multiplication" | "3":
            a,b = float(input("Enter first number: ")), float(input("Enter second number: "))
            product = multiply(a, b)
            print(f"The product is: {product}")
        case "division" | "4":
            a,b = float(input("Enter first number: ")), float(input("Enter second number: "))
            quotient = divide(a, b)
            print(f"The quotient is: {quotient}")
        case _:
            print("Invalid choice. Please select a valid operation.")

perform_operation(choice.lower())

print("\n----------------------------------------------")
