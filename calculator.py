from calculatortesting import *

#reference calculatortesting.py and test_calculatortesting.py
a = ""
b = ""

calc = Calculator()
def main_menu():
    print("Select Operation.")
    print("1. Addition.")
    print("2. Subtraction")
    print("3. Multiplication.")
    print("4. Division.")
    operator = input("Enter choice (1/2/3/4): ")
    return operator
operator = main_menu()

def add_numbers():
    a = int(input("Enter first whole number. \n::"))
    b = int(input("Enter second whole number. \n::"))
    print(calc.add(a,b))
def subtract_numbers():
    a = int(input("Enter first whole number. \n::"))
    b = int(input("Enter second whole number. \n::"))
    print(calc.subtract(a,b))
def multiply_numbers():
    a = int(input("Enter first whole number. \n::"))
    b = int(input("Enter second whole number. \n::"))
    print(calc.multiply(a,b))
def divide_numbers():
    a = int(input("Enter first whole number. \n::"))
    b = int(input("Enter second whole number. \n::"))
    print(calc.divide(a,b))

try:
    if operator == '1':
        add_numbers()
    elif operator == '2':
        subtract_numbers()
    elif operator == '3':
        multiply_numbers()
    elif operator == '4':
        divide_numbers()
except:
    print("Something went wrong. The monkeys are on it!")
