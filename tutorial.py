# Just print the output 
print ("Hello Python!")
print()
#############################################################################

# This will print true 
if 5 > 2: 
    print ("true") 
if 5 > 2: 
    print ("true") # This will print true 
print()

#############################################################################

# Multiline string is considered as comment 
"""
No worries!! 
It wont be executed since this counted as comment line 
Yayyyy
"""
#############################################################################

#Camel Case - first word starts with uppercase
myVariableName = "John"

#Pascal Case - each first word starts with uppercase
MyVariableName = "John"

#Snake Case - each word is separated by an underscore char
my_variable_name= "John"

print(my_variable_name)
print()

#############################################################################

#Assign Multiple Values 
x,y,z = "Apple", "Banas", "Cherry"
print(x)
print(y)
print(z)
print()

#Assign one vale to Multiple Variables
x = y = z = "Apple"
print(x)
print(y)
print(z)
print()

#Unpack a list of collection 
fruits = ["Apple", "Banas", "Cherry"]
x,y,z, = fruits
print(x)
print(y)
print(z)
print()

#############################################################################

#Output variable 
x = "awesome "
y = "and fun"
# + sign works for adding two values/numbers or adding 
# variable to another variable
z = x + y
print("Python is "+ z + "\n")
# Cons: Combining number + string will give an error

#############################################################################

#   Global Variables
# - can be used by everyone, both inside and outside of the functions
# Example 1
a = "funny"

def foo():
    print("He is " + a)
    print("")
foo()

#Example 2
a = "hello"
def foo1():
    a = "world"
    print("Well " + a)
    print()

foo1()
print("Well " + a)
print()

# Global keyword can be use to create global variable inside function
def foo2():
    global x
    x = "soup"

foo2()

print("I love "+ x)
print()

# Global keyword can be use to change the global variable inside a function
b = "again"

def foo3():
    global b
    b = "lol"

foo3()
print("Studying " + b)

#############################################################################

# Data types
# 1. Text Type:	str
str1 = "Hello world"
print(type(str1))
print()
str2=str("Hello world")
print(str2)
# 2. Numeric Types:	int, float, complex
num=5
print(type(num))
# 3. Sequence Types: list, tuple, range
# 4. Mapping Type:	dict
# 5. Set Types:	set, frozenset
# 6. Boolean Type: bool
# 7. Binary Types: bytes, bytearray, memoryview