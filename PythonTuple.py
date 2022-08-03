import this


thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))


thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#Update Tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Add Item
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

#Remove Item
thistuple =("apple", "banana", "cherry")
y = list(thistuple)
y.remove("cherry")
thistuple = tuple(y)
print(thistuple)

#Assign Red Value
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


#Tuple Loop
thistuple =("apple", "banana", "cherry")
for x in thistuple:
    print(x)
    

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])
    

#Join Tuple
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

###########
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


#Same as List just add{Bracket} Thats Why i skip this topics