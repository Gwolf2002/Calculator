import numpy as np


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mult(x, y):
    return x * y


def div(x, y):
    return x / y





print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Log")

while True:
    
    choice = input("Enter choice(1/2/3/4/5): ")

    
    if choice in ('1', '2', '3', '4', '5'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", mult(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", div(num1, num2))

        elif choice =="5":
            print ("log", num1, "+", num2, "=", np.log(num1 + num2))
        
        
        next_calculation = input("Do you want to do another calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
