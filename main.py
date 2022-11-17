#import the random module, hangman ascii art and words

import random
import hangman_art
import hangman_words
#print the logo
print(hangman_art.logo)

#make the choosen words random
chosen_word = random.choice(hangman_words.word_list)

#find the length of the choosen word

word_length = len(chosen_word)

#create a variable to use in determining the end of the game
end_of_game = False

#create a variable for the number of lives 
lives = 6

#Create a list
display = []

#add a dash to represent each word in the choosen word and add it to the list
for _ in range(word_length):
    display += "_"

#create a while loop using the end_of_game variable earlier created so that the questions will repeatedly come up
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    #introduce a conditional statement so that if the word has been previously entered, it will inform them.
    if guess in display:
      print(f'letter {guess} has been previously entered')
      
    #loop through the choosen word to replace the blanks with the correct letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            
    #this checks if user is wrong and deducts the lives with a feedback message.
    if guess not in chosen_word:
        lives -= 1
        print(
            f" you entered {guess} and it's not in the word."
        )
        print(f"You have {lives} lives left")
        if lives == 0:
            end_of_game = True
          
            print("You lose, you have no lives left ")
            print(f" The choosen word is {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
        print(f" The choosen word is {chosen_word}")

    #print the corresponding art to the number of lives left
    print(hangman_art.stages[lives])
