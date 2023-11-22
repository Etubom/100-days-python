# input() will get user input from console
# Then print() will print the word "Hello" and the user input
# print( "Hello " + input("What is your name?"))

# variables store our inputs/values
# name = input("What is your name?")
# print("Your name is "+ name)

# Use third var to perform switch
a = 10
b = 20
print("A at this point is: "+ str(a))
print("B at this point is:"+ str(b))

c = a
a = b
b = c
print("A at this point is now: "+ str(a))
print("B at this point is now:"+ str(b))

# variables
name = "Jack"
print(name)

name = "Angela"
print(name)

name = input("What is your name?")
length = len(name)
print(length)

# Band Name Generator
# 1 Create a greeting for your program.
print("Welcome to the band name generator bot")
# 2 Ask the user for the city that they grew up in.
city = input("What city did you grow up in?\n")
# 3 Ask the user for the name of a pet.
pet = input("What is the name of your pet?\n")
# 4 Combine the name of their city and pet and show them their band name.
print("Your band name is: "+city+pet)
# 5 Make sure the input cursor shows on a new line, see the example at:

