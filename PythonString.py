a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a) #Same as '''

#String Arrays

a = "Hello, World!"
print(a[1]) #Print e because H = 0, e = 1, l = 2 


#String Looping

for x in "Mahmudul":
    print(x)
    
#String length
x = "Mahmudul"
print(len(x))    

#Check String

txt = "Hello, My name is Mahmudul Hasan"
print("is" in txt) #print True

txt = "Hello, My name is Mahmudul Hasan"
if "is" in txt:
  print("TXT is present.")
else:
     print("TXT is not present.") 