High_score = input('Input The List Of Student Scores :').split()
for score in range(len(High_score)): 
    High_score[score] = int(High_score[score])
print(High_score)    
num = 0
for highScore in High_score:
    if highScore > High_score[num + 1]:
        x = highScore
    else:
        x = High_score[num + 1]
        
print(f"The High Score In The Class Is : {x}")        