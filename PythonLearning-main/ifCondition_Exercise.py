weight =int(input("Enter your weight : "))
height = float(input("Enter your height : "))

bmi=float((weight)/(height**2));

if(bmi<16.0):
    print("Severe Thinness")
elif(bmi>=16.0 and bmi<=16.9):
    print("Moderate Thinness")
elif(bmi>=17.0 and bmi<=18.4):
    print("Mild Thinness")
elif(bmi>=18.5 and bmi<=24.9):
    print("Normal range")
elif(bmi>=25.0 and bmi<=29.0):
    print("Pre-obese")
elif(bmi>=30.0 and bmi<=34.9):
    print("obese-1")
elif(bmi>=35.0 and bmi<=39.9):
    print("obese-2")
elif(bmi>=40.0):
    print("obese-3")
