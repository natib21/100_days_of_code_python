#Step 1 
import random,re
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word =word_list[random.randint(0, len(word_list)-1)]
print(chosen_word)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Enter a letter :")
guess.lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# x = re.findall(guess,chosen_word)
counter = 0
for x in range(0,len(chosen_word)- 1):
    if chosen_word[x] == guess:
        input("Enter a letter :")
        print(guess)
    else :  
        counter += counter
        print("You are not correct")
        if counter == len(chosen_word):
            break
        else:input("Enter A Letter :")  
   