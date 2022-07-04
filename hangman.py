import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

chosen_word = random.choice(word_list)
chosen_word_permanent = chosen_word
print(chosen_word) # You should delete this if you don't want to see the answer and play the game :p
hidden_word = ""
for i in range(0, len(chosen_word)):
  hidden_word += "_"
print(hidden_word)
lives = 6

while lives != 0 and chosen_word_permanent != hidden_word:
  
  guess_letter = input("Guess a letter that you think includes in the word?\n")
  
  if guess_letter in chosen_word: #If the answer is correct.
    for i in range(0,chosen_word.count(guess_letter)): #how many letter we found in guess_letter
      index_number = (chosen_word.index(guess_letter)) #spot the letter's index in chosen_word

      #change the letter in hidden_word
      g = list(hidden_word)
      g[index_number] = str(guess_letter)
      hidden_word = "".join(g)   
  
      #change the letter in chosen_word
      s = list(chosen_word)
      s[chosen_word.index(guess_letter)] = "/"
      chosen_word = "".join(s)
            
  else: #If the answer is not correct.
    lives -= 1
  
  if lives ==6:          #display hangman stages
    print(stages[6])
  elif lives==5:
    print(stages[5])
  elif lives==4:
    print(stages[4])
  elif lives==3:
    print(stages[3])
  elif lives==2:
    print(stages[2])
  elif lives==1:
    print(stages[1])
  elif lives==0:
    print(stages[0])

  print(hidden_word)  #display hidden_word
  
if lives == 0:
    print("Game Over. You lost!")
    print(f"Correct answer was {chosen_word_permanent}")
elif chosen_word_permanent == hidden_word:
    print("Congrats. You won!")
    print(f"You guessed the word: {chosen_word_permanent}")