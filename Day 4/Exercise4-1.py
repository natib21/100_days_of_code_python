import random

name_space = input("Give me everybody's name, seperated by comma. ")
names = name_space.split(",")
last_person = len(names)
pay_bills = random.randint(0,last_person - 1)
print(f'{names[pay_bills]} is going buy the meal today') 

