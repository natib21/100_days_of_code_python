
print(''' *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
******************************************************************************* 
 ''')
print('Welcome To The Tresure Island')
print('Your mission is to find the tresure')
direction = input("You're at a cross road. where do you want to go ? Type 'Left' or 'Right'\n")
direction.lower()
if direction == 'left':
    choose = input('You Come to the lake. There is an island in the middle of the lake.Type "Wait" to wait for the boat. type "Swim" to swim across.\n')
    choose.lower()
    if choose == 'wait':
        color = input('You arrive at the island unharmed. There is house with 3 doors. One red, One yellow and One blue. Which Color Do You Choose ?')
        color.lower()
        if color == 'yellow':
            print('You Win The Game')
        elif(color == 'blue' or color =='red'):
            print('you Enter a room of beast, GAME OVER!')
            
    else:
     print('GAME OVER!')            
else:
    print('you fell into a hole GAME OVER!')        
    