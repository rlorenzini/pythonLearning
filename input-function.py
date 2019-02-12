#user input; ask user for info and display it later

#input('')

#appears on terminal, and asks user to provide infoself.

#input('Enter first name')
#first_name = input('Enter First Name: ')

#variable first_name takes the value assigned by the user in the input function and assigns it to first_name.
#Any code that later calls on first_name will use the value assigned by the input function here.

#print("Welcome, " + first_name + ".")
#prints the value typed by the user into the input function


first_name = input('Enter First Name: ')
last_name = input('Enter Last Name: ')
print(first_name + " " + last_name + ", Welcome to your Terminal.")
age = 26

#functions/methods

#message = "Welcome to your Terminal, my Lord."
#print(message)

#message = "Welcome {name} to my Terminal. Time to slay some code!"
#print(message)


#defintion is def in PYTHON 3


#cannot call a function BEFORE it is created
#greet_user will NOT work above where greet_user was created
#MUST use : to create a function volume

def greet_user():
    #we are now inside the volume of the function
    #we MUST be one tab over to be INSIDE the function in PYTHON 3
#not inside a function in PYTHON 3
    print("Welcome to my Terminal.")
#creating a function to greet the user
#make sure variables and functions have names that make sense


greet_user()



def greet_with_name(name):
    print(f"Welcome {name} to my Terminal.")

greet_with_name("Richard")
greet_with_name("John")

#doing this allows you to inject multiple values into a single function.
#By placing print inside a function, you no longer have to type print(), but just the function name.


def greet_with_name_and_age(name, age):
    print(f"Welcome, {name} and your age is {age}.")


greet_with_name_and_age(first_name, age)

#will recall input(first_name) and age = 26, both previously defined variables.

#def greet_with_address(first_name, last_name, street, city, state, country):
#    print()


#When recalling functions, less is more. This is valid, but time consuming. (More info later)

#functions with optional arguments
def greet_with_optional_age(name, age = 32):
    print(f"{name} and age is {age}")
    #do NOT forget f"" when using {}

greet_with_optional_age('Mary', 34)

#age = 32 is the optional argument. If you do not pass a value to age, 32 will be the default age displayed.
#If age is defined in function, it will be replaced. 34 will be displayed instead of 32.



#functions that return a value

#basic math functions are examples of functions returning values
#return is used to store values of functions to be recalled later

def add(a,b):
    return a+b
    print("What about me?")
    #anything done AFTER a return will NEVER be executed, meaning print() will not be displayed
    #sum = a+b
    #return sum
    #another way to do it, where you return the value of sum, but NOT sum as a variable.
    #anything INSIDE a function ONLY gets recalled through that specific function and nowhere else



result = add(3,5)

result = result * 10
print(result)
#if we did not define result OUTSIDE the function then print(result) would NOT work
#add(3,5)
#print(result)
#this would have an error stating result is not defined


#def add(a,b):
#    return (a+b)

#add(2,3)
#follows the math principles; multiplies before adds, etc.
#The value of a+b is stored on the left. a+b works, but return a+b stores the value in return to be used later



name = "John"

def change_name():
    global name
    #global is used to change the value of name
    name = "Mary"

change_name()
print(name)

#name still has the value of John and will not display Mary.
#global allows us to change values outside of the function, but is not considered good practice

#TRUPLE


def airport_name_and_code():
    return ("Intercontinental Airport", "IAH") #truple

(airport_name, airport_code) = airport_name_and_code()
#this can be used to assign values of a return
print(airport_name)
print(airport_code)

#NOTE: your function should do ONE and ONLY ONE thing to avoid complications

#bad example of a function below which does too much at once

#def send_diagonstics():
    #code to send email
    #code to send fax
    #code to send message

#when trying to send an email, you cannot call on send_diagnostics
#you have to GO TO send_diagnostics and COPY the send email code to send an email

#def send_diagnostics():
    #send_email()
    #send_fax()
    #send_message()

#send_email()



#def add(no1,no2):
    #result = no1 + no2
    #print(result)

#add is now responsible for printing the result of add
#if you call add later, print() will always occur even if you do not want it to


#def add(no1,no2):
    #print("--------------")
    #pint(f"{no1} + {no2} = {result}")
    #print("--------------")


#def subtract(no1,no2):
    #print("--------------")
    #pint(f"{no1} - {no2} = {result}")
    #print("--------------")

#any changes you need to make to the print() now takes longer

def add(no1,no2):
    result = no1 + no2
    operator = "+"
    return no1 + no2


def display_result(no1,operator,no2):
    print("--------------")
    pint(f"{no1} {operator} {no2} = {result}")
    print("--------------")
#THIS IS AN EXAMPLE AND DOES NOT DISPLAY PROPERLY  

#display is now responsible for displaying the results of the previous functions
#you only need to change display to change the display of the results
#you no longer have to go back and change the print() from addition, subtraction, etc
#this is the benefit of keeping functions on a singular focus
