age = input("What is your age ? \n" )

age_Left = 90 - int(age)  

day = 365 * age_Left
week = 52 * age_Left
month = 12 * age_Left

print(f"you have left {day} days , {week} week , and {month} month left.")


