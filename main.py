import random
import hangman_art
import hangman_words
import os


chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

display = []

for _ in range(word_length):
    display += "_"
while not end_of_game:

    guess = input("Guess a letter: ").lower()
    if guess in display:
        print("You've already guessed this letter.")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:

        print(
            f"The letter you chose {guess}, is not in the word, you lose a life."
        )
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")


    print(hangman_art.stages[lives])



#I need to add section wise hints.


