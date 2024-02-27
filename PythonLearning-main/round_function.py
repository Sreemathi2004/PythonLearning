"""
21.344=>21
21.67=>22

rount(number,no_of_digits)
"""
print(int(round(21.67,0)))
print(round(7,2))
print(round(2.6666,2))
print(round(2.6678,0))
print(round(7.5)) #8
print(round(6.5)) #if the round of value is even then only it convert ,6,7 =>6
print(round(11.5))
print(round(12.5))
print(round(674,2))
print(round(674,0))
print(round(674,-1)) # 10^(-no of digits) => 10^(-(-1))=>10^1=>10
print(round(665,-1))#even
print(round(675,-1))#even
print(round(-8/3))
print(round(-8/3,2))
print(round(675,1))
print(round(673,1))
print(round(674.1012,-1))
print(round(1212,-2))
print(type(round(6.777)))