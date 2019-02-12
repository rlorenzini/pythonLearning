#print('does this work too?')
#Can use "" or '' interchangeably.




#Data Types

# hidden
#name = "John"
#print(type(name))

#pi = 3.142
#isOpen = True

#print(pi)
#print(isOpen)



first_name = "John"
last_name = "Doe"
#full_name = first_name + last_name
age = 26
#script runs as "John" + "Doe" and displays as JohnDoe
#print(full_name)
#full_name2 = first_name + "," + last_name
#will display as John, Doe
#print(full_name2)


#strings are immutable (cannot be changed)
#full_name is not CHANGING the values of first_name and last_name, but creating a NEW string


#print(string1 + string2 + string3 + ...)


#string interopolation
#you can create strings by injecting variables in different places

#full_name = f"{first_name},{last_name}"

#code is saying inject the values into the variables with a comma in the middle.

full_name = f"My first name is {first_name} and my last name is {last_name} and my age is {age}"
print(full_name)

#full_name2 = "My first name is " + first_name + "and my age is " + age
#print(full_name2)
#error message displays for print(full_name2). age is an integer and cannot be changed to string as is.
#use str() to change age to a string.


full_name2  = "My first name is " + first_name + " " + "and my age is " + str(age)
print(full_name2)
