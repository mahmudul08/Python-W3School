#Allow Duplicates
list = ["apple", "banana", "cherry", "apple", "cherry"]
print(list)

#List Length
list = ["apple", "banana", "cherry", "apple", "cherry"]
print(len(list))

#Type
mylist = ["apple", "banana", "cherry"]
print(type(mylist))


##Access Items

list = ["apple", "banana", "cherry"]
print(list[1])

list = ["apple", "banana", "cherry"]
print(list[1])


#Two to Five Item will be print
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


#Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
thislist = ["apple", "banana", "cherry"]
if "Orange" in thislist:
  print("Yes fruits is in the fruits list")
else:
    print("No fruits is not in the fruits list") 
    
    
    
#Change  Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Insert New Value
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Append Item its mean add last
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["Mahmudul", "Hasan"]
tropical = ["Abdullah", "Zabir"]
thislist.extend(tropical)
print(thislist)

#Add Any iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#Remove Specific index(POP)
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Remove Last Item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#Remove Specific Index(del)
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist

#Clear List
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


#LOOP LIST
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#WHILE LOOP
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
    
#FOR LOOP
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#List comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

