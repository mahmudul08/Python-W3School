# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b


###########
a = 33
b = 50

if  b > a:
    print("B ia greater than A")
    
###########
a = 33
b = 50

if  a > b:
    print("B ia greater than A")
else:
    print("A is greater than B")    
    
    
######################
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


######################
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else: 
    print("A is greater than B") 
    
    
#AND
a = 33
b = 15
c = 66
if a > b and c >a: 
    print("Both condition is true")
    
    
#OR
a = 33
b = 15
c = 66
if a > b or c >a: 
    print("At least one condition is true")
    
#Nested if
x = 41

if x > 10:
    print("Above Ten")
    
    if x > 20:
        print("And also above 20!")
    else:
       print("But not above 20")
       
#PASS Statement
a = 33
b = 200
if b > a:
    pass                        