#Creating a Function
import re
from unittest import result


def my_function():
    print("Hello from function")
    
my_function()   


#Arguments
def my_function(fname):
     print(fname + " Mahmudul Hasan")
   
my_function("Email")
my_function("Phone")
my_function("Facebook")     
    
    
def my_function(fname, lname):
    print(fname + " " + lname)
    
my_function("Mahmudul", "Hasan")    
        
        
        
#Arbitrary arguments
def my_function(*kids):
      print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")  

##############
def my_function(*kids):
    print("The youngest child is " + kids[0])
    
my_function("Mahmudul", "Hasan", "Mohammad")   


#Default Parameter
def my_function(country = "Norway"):
      print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Passing a List as an Argument
def my_function(food):
    for x in food:
        print(x)
        
fruits = ["apple", "orange", "orange", "orange"]
my_function(fruits)


#Return Value
def my_function(x):
      return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9)) 

#Recursion
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k-1)
        print(result)
        
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6) 


#Lambda Function
def myfunction(n):
    return lambda a : a * n

mydoubler = myfunction(3)
mydoubler = myfunction(4)

print(mydoubler(11))
print(mydoubler(4))
           
           
           