x = float(input("Enter the first number: "))
print(" ")
y = float(input("Enter the second number: "))
print(" ")

print("Type 1 to add.")
print("Type 2 to subtract.")
print("Type 3 to divide.")
print("Type 4 to multiply.")
operation = int(input("Which operation do you want to perform? "))

def add(x, y):
    add = x + y
    print("Your answer is: ", x, "+", y, "=", add)

def subtract(x, y):
    subtract = x - y
    print("Your answer is: ", x, "-", y, "=", subtract)

def divide(x, y):
    divide = x / y
    print("Your answer is: ", x, "/", y, "=", divide)

def multiply(x, y):
    multiply = x * y
    print("Your answer is: ", x, "*", y, "=", multiply)

if operation == 1:
    add(x, y)

if operation == 2:
    subtract(x, y)

if operation == 3:
    divide(x, y)

if operation == 4:
    multiply(x, y)

elif operation>=5:
    print("Enter either 1, 2, 3 or 4 only.")