def multiply(a, b):
    return a * b

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def div(a,b):
    return a / b

num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number 2: "))
print(f"The Addition of two numbers are: {add(num1,num2)}")
print(f"The Difference of two numbers are: {sub(num2,num1)}")
print(f"The Multiplication of two numbers are: {multiply(num1,num2)}")
print(f"The Quotient of two numbers are: {div(num1,num2)}")