roll_no=[1,2,3,4,5,6,2,1,99,12,2]
names=["Sreemathi","Kavitha","Karthika"]
mix_list=[1,"Jenny",True,10.10]
# list => dynamically sized array
#list => mutatable => change
#list => ordered

print(roll_no)
print(roll_no[0])
print(mix_list[-2])

print(roll_no[:3])
print(roll_no[1:])

roll_no.append(78)
print(roll_no)
print(roll_no[0:5:2])#steps
print(roll_no[0::2])
roll_no.sort()
print(roll_no)
roll_no.reverse()
print(roll_no)

# mixedlist is not allowed for sorting

roll_no.insert(2,45)
print(roll_no.reverse())
print(roll_no)

roll_no.extend([34,78,90,23,100,167])
print(roll_no)
roll_no.reverse()
print(roll_no)
roll_no.sort()

print(roll_no)
print(len(mix_list[1]))

print(max(roll_no))

print(len(roll_no))
print(roll_no.index(167))
roll_no[0]=0
print(roll_no)

roll_no[0:4]=[3,4,5,6,7]
print(roll_no)
roll_no.remove(2)
print(roll_no)
print(roll_no.pop())
print(roll_no.pop(1))
print(roll_no)

