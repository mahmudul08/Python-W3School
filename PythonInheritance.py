from inspect import classify_class_attrs


class Person:
      def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
      def print_name(self):
         print(self.firstname, self.lastname)
         
class Student(Person):
    pass         
               
x = Student("Mahmudul", "Hasan")
x.print_name()



##############
class Person:
      def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

      def print_name(self):
            print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduation_year = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduation_year)

x = Student("Mahmudul", "Hasan", 2022)
x.welcome()



#PYTHON ENHERITANCE 
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

####################
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


###############
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)
    
#################
mystr = "banana"

for x in mystr:
  print(x)
  
##############
class MyNumber:
    def __iter__(self):
        self.a = 1
        return self
    
    def  __next__(self):
        x = self.a
        self.a += 1
        return x
    
myclass = MyNumber()
myiter = iter(myclass)

print(next(myiter)) 
print(next(myiter))  
print(next(myiter))  
print(next(myiter))  
print(next(myiter)) 


#PYTHON SCOPE
def myfunc():
    x = 300
    print(x)
myfunc()


############
def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()    
myfunc() 

#############
x = 3000
def myfunc():
    x = 200
    print(x)
myfunc()
print(x)

##############
def myfunc():
    global x
    x = 300
myfunc()
print(x)

############
x = 300000
def myfunc():
    global x
    x = 200
myfunc()
print(x)    
            
        
          
