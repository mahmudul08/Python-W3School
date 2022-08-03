#Text Type = str
#Numeric Type = int, float, complex
#sequence Type = list, tuple, range
#mapping Type = dict
#Set Type = set, frozenset
#boolean Type = bool
#Binary Type = bytes, bytearray, memoryview
#None Type = NoneType

a = "Hello World" #str
b = 20 #int
c = 20.5 #float
d = 1j #Complex
e = ["apple", "banana", "cherry"] #list
f = ("apple", "banana", "cherry") #tuple
g = range(6) #range
h = {"name" : "John", "age" : 36} #dict
i = {"apple", "banana", "cherry"} #set
j = frozenset({"apple", "banana", "cherry"}) #frozenset
k = True #Boolean

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))
