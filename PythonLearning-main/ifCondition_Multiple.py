"""
if condition1:
    do X
if condition2:
    do Y
if condition3:
    do z
"""

Order=input("Small Pizza : 100 \n Medium Pizza : 200 \n Large Pizza : 300  'Please any of the dishes'")
bill=0;
check=input("Do you need pepperoni ??(Y/N) : ")
if(check=='Y' or check =='y'):
    if(Order == "Small Pizza"):
        print(f"Total Bill : {100+30}")
    if(Order == "Medium Pizza"):
        print(f"Total Bill : {200+50}")
    if(Order == "Large Pizza"):
        print(f"Total Bill : {300+20}")
else:
    print("Just i need pizza alone")
