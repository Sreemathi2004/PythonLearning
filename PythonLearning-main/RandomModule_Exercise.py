#head or tail game

import random
choosing=random.randint(0,1)
if(choosing==1):
    print("Head")
else:
    print("Tail")


# select a random name from a list of names and the person selected will have to pay for everybody's food bill

names ="sree,akshaya,karthi,kavi"
list=names.split(",")
name=random.randint(0,3)
print(f"{list[name]} will pay the bill")

name=random.choice(list)
print(f"{name} will pay the bill")

