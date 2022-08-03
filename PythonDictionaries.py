########
thisdict = {
    "brand": "Ford",
    "Model": "Mustang",
    "year": 1944
}
print(thisdict)

############
thisdict = {
    "brand": "Ford",
    "Model": "Mustang",
    "year": 1944
}
print(thisdict["brand"])

#Dictionary length
thisdict = {
    "brand": "Ford",
    "Model": "Mustang",
    "year": 1944
}
print(len(thisdict))

#Data Type
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(type(thisdict))


#Accessing Items
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
x = thisdict["brand"]
print(x)


#Get
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
x = thisdict.get("brand")
print(x)

#key
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
x = thisdict.keys()
print(x)

#Values
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
x = thisdict.values()
print(x)

#Value change
car = {
    "brand": "Ford",
    "Model": "Mustang",
    "year": 1944
}
x = car.values()
print(x)
car["year"] = 1922
print(x)



#########
car = {
    "brand": "Ford",
    "Model": "Mustang",
    "year": 1944
}
x = car.items()
print(x)
car["year"] = 1922
print(x)

#Update values
car = {
    "brand": "Ford",
    "Model": "Mustang",
    "year": 1944
}
car.update({"year": 1950})
print(car)

#Change values
car = {
    "brand": "Ford",
    "Model": "Mustang",
    "year": 1944
}
car["year"] = 2022
print(car)

#Adding Items
car = {
    "brand": "Ford",
    "Model": "Mustang",
    "year": 1944
}
car["color"] = "Red"
print(car)

#Remove Items
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)

#Copy
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#Nested
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
