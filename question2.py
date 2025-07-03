def add(num1: float, num2: float) -> float:
    result = num1 + num2
    return result

def subtract(num1: float, num2: float) -> float:
    result = num1 - num2
    return result

def multiply(num1: float, num2: float) -> float:
    result = num1 * num2
    return result

def divide(num1: float, num2: float) -> float:
    if num2 == 0:
        print("Error: Cannot divide by zero")
    else: 
        result = num1 / num2
    return result
        

def simple_calculator(num1: float, num2: float, choice: int):
    if choice == 1:
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif choice == 2:
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif choice == 3:
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif choice == 4: 
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")

print("Simple Calculator")
print("=================")

while True:
    print("\nCalculator Menu: ")
    print("1. Add \n2. Subtract \n3. Multiply \n4. Divide \n5. Exit")
    choice = input("Choose an opperation: ")

    try:
        choice = int(choice)
    except ValueError:
        print("Please enter a valid choice")
        continue

    if choice > 5 or choice < 1:
        print("Please enter a value 1-5")
        continue

    if choice == 5:
        print("Thank you for using the calculator!")
        break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    simple_calculator(num1, num2, choice)
        
