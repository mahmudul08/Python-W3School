#True or false
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 300

if a > b:
    print("A is greater than B")
else:
    print("B is greater tha A") 
    


x = "Hello"
y = 15

print(bool(x))
print(bool(y))

class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))



def myFunction():
      return True

if myFunction():
  print("YES!")
else:
  print("NO!")


def myFunction():
      return False
  
if myFunction():
  print("YES!")
else:
  print("NO!")