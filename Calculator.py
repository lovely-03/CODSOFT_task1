def add(a, b):
    #This function adds two numbers
    return a + b

def subtract(a, b):
    #This function subtracts two numbers
    return a - b

def multiply(a, b):
    #This function multiplies two numbers
    return a * b

def divide(a, b):
    #This function divides two numbers
    if b == 0:
        return "Error! Can't divide by zero."
    else:
        return a / b

while True:
    #Take input from the user
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("\nEnter second number: "))
    op = input("\nEnter operation( + , - , * , / ): ")

    #Perform the calculation
    if op == '+':
        print(f"\n{num1} + {num2} = {add(num1, num2)}")

    elif op == '-':
        print(f"\n{num1} - {num2} = {subtract(num1, num2)}")

    elif op == '*':
        print(f"\n{num1} * {num2} = {multiply(num1, num2)}")

    elif op == '/':
        print(f"\n{num1} / {num2} = {divide(num1, num2)}")
    
    else:
        print("Invalid Input")

