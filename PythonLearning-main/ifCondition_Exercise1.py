# check whether give year is leap year or not

# 1) divisible by 4 -> yes
#         divisible by 100 -> yes
#               divisible by 400 yes

year =int(input("Which year you want to check : "))
if(year %4==0):
    if(year%100==0):
        if(year%400==0):
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")