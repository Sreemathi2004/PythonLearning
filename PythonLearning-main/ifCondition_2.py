"""
if condition1:
    statement1
    if condition2:
        statement2
    else
        statement3
else
    statement4



if condition1:
    statement1
elif condition2:
    statement2
elif condition3:
    statement3
else:
    statement4
"""

height=int(input("What is your height in feet : "))
if height>=3:
    print("You can ride")
    age=int(input("What is your age ? "))
    if(age<12):
        print("pay Rs.15")
    elif(age>12 and age<=18):
        print("pay Rs.250")
    else:
        print("pay Rs.500")
else:
    print("Don't Ride")
print("End")