Partner_name1 = input("Enter the partner1's name")
Partner_name2=input("Enter the partner2's name")
combine_string = Partner_name1 + Partner_name2
Lower_case=combine_string.lower()

t=Lower_case.count('t')
r=Lower_case.count('r')
u=Lower_case.count('u')
e=Lower_case.count('e')
true=t+r+u+e

l=Lower_case.count('l')
o=Lower_case.count('o')
v=Lower_case.count('v')
e=Lower_case.count('e')
love=l+o+v+e

lovepercent=str(true)+str(love)
lovepercent=int(lovepercent)
if(lovepercent<10 or lovepercent>90):
    print("Like coke and mentos")
elif(lovepercent>=40 and lovepercent<=50):
    print("Alright together")
else:
    print("okay")