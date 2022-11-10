#Let's build hangman
import random
import words
import art


pick = random.choice(words.word_list)

#Test code:
print(pick)
print(art.logo)
#Variables:
not_win = True
display = []
lives = 6

for i in range(0, len(pick)):
  display.append("_")
print(display)

while not_win:
  player_guess = input("\nPlease guess a letter.\n\n").lower()

  count = 0
  for letter in pick:
    count += 1
    if player_guess == letter:
      if player_guess in display:
        print("\n\nYou already guess that.")
      else:
        display[count-1] = letter
    
    
    
  print(f"\n{display}\n") 

  if "_" not in display:
        not_win = False
        print("You won!")
  if player_guess not in pick:
      print("You are wrong\n") 
      lives -= 1
      #print(art.stages[lives])
      if lives == 0:
        print("\n You lost! \n\n")
        not_win = False
      else: 
        print(f"You lost a life. Lives left: {lives}")
  
  
  
      
# Need sort out words with double letters.
# I need to add section wise hints.


