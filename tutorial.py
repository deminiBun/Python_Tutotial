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

#############################################################################

#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(x)

print(x)
print(y)
print(z)
print()
print(type(x))
print(type(y))
print(type(z))
print()

#############################################################################

#import random module and display a random number between 1-9
import random
print(random.randrange(1, 10))
print()

#############################################################################

int1 = int(2.8)
int2 = int("3")
fl1 = float(1)
fl2 = float("4.2")
fl3 = float("3")
st1 = str("s1")
st2 = str(2)
st3 = str(3.0)
print(int1, int2, fl1, fl2, fl3, st1,st2,st3)
print()

#############################################################################

# String can be surrounded by "" or ''
# both will print the same output
print("hello")  
print('hello')

#############################################################################

# Multiline string
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print()

#############################################################################

# Strings are arrays
a = "Hello World"
print(a[1])
print(a[4])
print()

#############################################################################

# Loop through a string
for x in "banana":
    print(x)

#############################################################################

# String length
hey = "Whatsupp"
print(len(hey))

#############################################################################

# Check string
txt = "The best things in life are free"
print("free" in txt)  #in represents certain phrase or char is present in a string
print()

#use if statement
txt = "The best things in life are free"
if "freed" in txt:
    print("'free' is present.") 
    print()  #nothing prints out since freed DNE

#print only if "expensive" is NOT present
txt = "The best things in life are free"
if "expensive" not in txt:
    print("'expensive' is NOT present.") 
    print() 

#############################################################################

# Slicing: return range of chars using slice syntax
# Return chars from position 2 to 5(exclude)
test = "Hello, world"
print(test[2:5])
print()

#Get the chars from the start to pos 5(excluded)
print(test[:5])
print()

#Get the chars from pos 2 onwards
print(test[2:])
print()

# Negative Indexing : Start from the end of the string
print(test[-5:-2])
print()

#############################################################################

# Uppercase 
print(test.upper())
# LowerCase
print(test.lower())
# Remove whitespace from beginning or the end
test1 = "   Hello    world    "
print(test1.strip())
# Splits the string into substring if it finds instances of separator
print(test.split(",")) # returns ['Hello', ' world']
