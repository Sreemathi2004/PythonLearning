"""
randint(a,b)  --> a<=x<=b
randrange(a,b) --> a<=x<b
random() -->  0.0<=x<1.0
uniform()
choice()
shuffle()
"""

import random
a=random.randint(1,3)
print(a)

b=random.randrange(1,4)
print(b)

c=random.random()
print(c)

d=random.uniform(1,3) #floating number
print(d)

l=[2,5,90,-5,89,12,56]
a=random.choice(l)
print(a)
random.shuffle(l)
print(l)