age = 23
txt = "My name is Mahmudul, and I am {}"
print(txt.format(age))

quantity = 5
itemno = 100
price = 99.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


#Nnumer 2 for price, 0 for quantity, 1 for itemno
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))