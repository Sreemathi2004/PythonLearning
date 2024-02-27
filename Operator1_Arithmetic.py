"""
+ - * / %
#in python 5/2 =>2.5 instead of / this we use //->floor division to change interger number
#power => ** print(2**3) = 8

BODMAS
    ()
    ** ->POWER
    * / // %
    + -
    5+2*3-1+10/5 =>5+6-1+2.0 =>11-1+2.0 =>10+2.0 =>12.0
"""
num1=input("Enter the number1 : ")
num2=input("Enter the number2 : ")

#Addition
print((int(num1)+int(num2)))
#Subtract
print((int(num1)-int(num2)))
#Multiplication
print((int(num1)*int(num2)))
#Division
print((int(num1)//int(num2)))
#Modulo
print((int(num1)%int(num2)))
#Power
print((int(num1)**int(num2)))

#Exercise calculate BMI
#Formula =(weight)/(height)^2
weight=input("Enter your weight : ")
height=input("Enter your height : ")
BMI = float( int(weight)/(int(height)**2));
print(BMI)