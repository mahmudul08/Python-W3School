################
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
 ########
for x in "Banana":
     print(x) 
     
#Break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
      break

##########
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
      break  
  print(x)
  
##########
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
      continue  
  print(x)        


#Nested Loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)