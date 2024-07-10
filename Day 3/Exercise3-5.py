print("Welcome to The Love Calculator")
Your_Name = input("What Is Your Name \n? ")
his_her_Name = input("What Is Their Name \n ? ")
together_Name =(Your_Name + ""+ his_her_Name).lower()
first = 0
second = 0
print(together_Name)
t = together_Name.count('t')
r = together_Name.count('r')
u = together_Name.count('u')
e = together_Name.count('e')
l = together_Name.count('l')
o= together_Name.count('o')
v= together_Name.count('v')
E= together_Name.count('e')
first = t + r + u + e
second = l + o + v + E

love_score = f"{first}{second}"
  
if(int(love_score) < 10 or int(love_score) > 90):
    print(f"Your Score is {love_score}, you go together like coke and mentos.")
elif(int(love_score) > 40 and int(love_score) < 50):
    print(f"Your Score is {love_score}, you are alright together")
else:
    print(f"You Score is {love_score}")        