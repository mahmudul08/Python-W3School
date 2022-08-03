'''
#Creating Variables
x = float(input('Enter Any Digit : '))
y = str(input('Enter any Name : '))

result = x
result1 = y

print('Digit is : ', result)
print('Name is : ', result1)

'''

'''
#Casting Variables
x = str('3')    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)

'''

#Get Type
'''
x = (input('Enter Any Digit : '))
y = (input('Enter any Name : '))

result = x
result1 = y

print(type(result))
print(type( result1))

'''

'''
x = 5
y = "John"
print(type(x))
print(type(y))

'''

"""
#Multiple Values

x = y = z = "Orange"
print(x)
print(y)
print(z)
"""

"""
#Unpack Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)

Name = ["Mahmudul Hasan", "Abdullah", "Zabir"]
x, y, z = Name

print(x)
print(y)
print(z)

"""

#Output Variables
"""
x = "Python"
y = "is"
z = "awesome"

print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y ='jhon'
print(x, y)

"""

#Global Variables
"""
x = 'Awesome'

def myfunc():
    x = 'Fantastic'
    print('Python is ' + x)
    
myfunc()
print('Python is ' + x) 

"""  

def myfunc():
    global x
    x = 'Fantastic'
myfunc()
print('Python is ' + x)


x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
    