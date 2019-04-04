#import
from math import *

#Print to console

print("Hello World")

#Variables

character_name = "John"
character_age = "35"
isKey = True
number = 5


print( "\nPlayer Name:" + character_name + "\nPlayer age: " + character_age)
print(character_name[0])

#Get input from user
#name = input("Enter your name: ")
#age = input("Enter your age: ")

#print("Hello: ", name + "(" + age +")")

#num1 = input("Enter num: ")
#num2 = input("Enter another num: ")

#result = int(num1) + int(num2)

#print(result)

#Array

friends = ["Andre", "Shante", "Pookie"]
friends.append("Crystal")
friends.insert(-1, "Nienie")
print(friends)
print(friends[-1])#selects last at index
print(friends[0:2])#swlects list between those numbers
friends.clear()
print(friends)

#Tuple
cordinates = (7, 10, 0)
print(cordinates[1])
print(cordinates)

#Functions
def say_Hi():
    print("Hi")

say_Hi()

def add(num1, num2):
    return num1 + num2

print(add(10, 25))

#If statements

is_male = True
is_tall = True

if is_male:
    print("True")
else:
    print("False")

if is_male or is_tall:
    print("Is tall or male")

if is_male & is_tall:
    print("Is male and tall")

if is_male and not is_tall:
    print("Is male and not tall")


if is_tall:
    print("Is tall")
elif is_male:
    print("Is male")
elif is_tall and not is_male:
    print("Is tall and not male")