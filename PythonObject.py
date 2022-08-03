class Myclass:
    x = 5
p1 = Myclass()    
print(p1.x)

##################
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p1 = Person("Mahmudul Hasan", 23)

print(p1.name)
print(p1.age) 


##################
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def my_func(self):
         print("Hello my name is " + self.name)
        
p1 = Person("Mahmudul", 23)
p1.my_func() 


##################
   
                  
    