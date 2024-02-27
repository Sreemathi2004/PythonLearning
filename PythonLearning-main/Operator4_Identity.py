"""
 is , is not
 it checks whether the memory addresses are same or not

 == this compares just value
 is this compare memory address
"""

a=5
b=5
print(a is not b)
print(id(a)) # it shows memory address
print(id(b)) #it shows memory address
a1=5
a2='5'
print(a1 is not a2)

print(id(a) == id(b))
print(id(a1)==id(a))
print(id(a1) is id(a))
a=6
print(id(a))

