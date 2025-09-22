x = 5
y = "Alex"

# print(x)
# print(y)

# Assign multiple variable
x, y, z = "Orange" , "Mango", "Banana"
# print(x)
# print(y)
# print(z)

x = y = z = "Apple"
# print(y)

cars = ["BMW" , "MERCEDES", "AUDI"]
x, y, z = cars
# print(x)
# print(y)
# print(z)

# output variables
x = "Python"
y = "is"
z = "awesome"
# print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
# print(x + y + z)

# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.

#GLOBAL VARIABLE

x = "awesome"
def city():
    print("Oslo city is" + x)
# city()

x = "awesome"

def some_city():
    x = "Dangerous"
    print("Milan is " + x)

# some_city()

# print("Rome is " + x)

# Global keyword



def my_city():
    global x 
    x = "Awesome"
# my_city()
# print("My home city is " + x)


x = "Awesome"

def your_house():
    global x
    # x = " Fantastic"
your_house()
print("Your house is " + x)