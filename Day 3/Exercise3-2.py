height = float(input("What is Your Height in M: ? "))
weight = float(input('What is Your Weight in KG: ?'))

BMI = weight / height ** height

if BMI < 18.5:
    result ="underWeight"
elif BMI > 18.5 and BMI < 25:
    result = "normal weight"
elif BMI > 25 and BMI < 30:
    result ="overWeight"  
elif BMI > 30 and BMI < 35:
    result ="obese"   
else:
    result ="clinically obese"   
       

print(f"Your BMI is : {round(BMI,1)} and you are {result}")

