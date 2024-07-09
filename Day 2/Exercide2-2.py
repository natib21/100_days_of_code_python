height = input('enter your height in m: ')
weight  =input('enter your weight in kg: ')
BMI = float(weight)/float(height) ** float(height)

print(BMI)

print(round(BMI, 2))