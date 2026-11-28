# def greet():
#     print("I am feeling sleepy")
#
# greet()
# greet()
#
#
# def greet(name):
#     print(f"Hello {name}")
#
# greet("siva")
#
# def show_double(n):
#     print(n*2)
#
# def get_double(n):
#     return n*2
#
# show_double(10)
# value = get_double(10)
# print(value)


## Simple Calculator


def add(a, b):
    return a + b

def subract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def reminder(a , b):
    return a % b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
sign = input("Enter operation: ")

if sign == "+":
    print(a + b)

elif sign == "-":
    print(a - b)

elif sign == "*":
    print(a * b)

elif sign == "/":
    print(a / b)

elif sign == "%":
    print(a % b)


