<h1>Hangman Game in Python</h1>
<p>In this tutorial, we will create a simple hangman game in Python. The game will randomly select a word from a pre-defined list of words and the player will have to guess the word by guessing individual letters. The game will keep track of the number of lives remaining and will display ASCII art corresponding to the number of lives remaining. The game will end when the word has been fully guessed or when the player runs out of lives.</p>
<h2>Prerequisites</h2>
<ul>
  <li>Basic knowledge of Python programming</li>
  <li>Familiarity with loops and conditional statements</li>
</ul>
<h2>Setting up the project</h2>
<ol>
  <li>Create a new Python file and name it <code>hangman.py</code>.</li>
  <li>At the top of the file, import the following modules:
  <pre><code>import random
import hangman_art
import hangman_words</code></pre></li>
  <li>Next, we will print the logo by printing the <code>logo</code> attribute of the <code>hangman_art</code> module:
  <pre><code>print(hangman_art.logo)</code></pre></li>
</ol>
<h2>Selecting a word</h2>
<ol>
  <li>To select a word, we will use the <code>random.choice()</code> function to choose a random word from the <code>word_list</code> attribute of the <code>hangman_words</code> module:
  <pre><code>chosen_word = random.choice(hangman_words.word_list)</code></pre></li>
  <li>We will also need to know the length of the chosen word, so we will store it in a variable called <code>word_length</code>:
  <pre><code>word_length = len(chosen_word)</code></pre></li>
</ol>
<h2>Setting up the game loop</h2>
<ol>
  <li>Next, we will create a variable called <code>end_of_game</code> and set it to <code>False</code>. This variable will be used to determine when the game should end. We will also create a variable called <code>lives</code> and set it to <code>6</code>, which will represent the number of lives the player has remaining.
  <pre><code>end_of_game = False
lives = 6</code></pre></li>
  <li>We will create a list called <code>display</code> to store the current state of the word. Initially, the word will be represented by a series of underscores, one for each letter in the word. We will use a <code>for</code> loop to add underscores to the list:
  <pre><code>display = []
for _ in range(word_length):
    display += "_"</code></pre></li>
  <li>Now we will set up the main game loop using a <code>while</code> loop and the <code>end_of_game</code> variable.
  
  <ol start="3">
  <li>Inside the game loop, we will prompt the user to guess a letter and store it in a variable called <code>guess</code>. We will also convert the guess to lowercase to make it case-insensitive:
  <pre><code>while not end_of_game:
    guess = input("Guess a letter: ").lower()</code></pre></li>
</ol>
<h2>Checking the guess</h2>
<ol>
  <li>Inside the game loop, we will check if the letter has already been guessed by the player. If it has, we will print a message to inform the player:
  <pre><code>if guess in display:
    print(f'letter {guess} has been previously entered')</code></pre></li>
  <li>Next, we will loop through the chosen word and check if the guessed letter is present in the word. If it is, we will replace the corresponding underscore in the <code>display</code> list with the letter:
  <pre><code>for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter</code></pre></li>
  <li>If the guessed letter is not present in the word, we will decrease the number of lives remaining and print a message to inform the player:
  <pre><code>if guess not in chosen_word:
    lives -= 1
    print(f" you entered {guess} and it's not in the word.")
    print(f"You have {lives} lives left")</code></pre></li>
</ol>
<h2>Ending the game</h2>
<ol>
  <li>If the player runs out of lives, we will set the <code>end_of_game</code> variable to <code>True</code> and print a message to inform the player that they have lost:
  <pre><code>if lives == 0:
    end_of_game = True
    print("You lose, you have no lives left ")
    print(f" The choosen word is {chosen_word}")</code></pre></li>
  <li>We will also check if the player has successfully guessed all the letters in the word. If they have, we will set the <code>end_of_game</code> variable to <code>True</code> and print a message to inform the player that they have won:
  <pre><code>if "_" not in display:
    end_of_game = True
    print("You win.")
    print(f" The choosen word is {chosen_word}")</code></pre></li>
</ol>
<h2>Displaying the current state of the game</h2>
<ol>
  <li>Inside the game loop, we will print the current state of the word by joining all the elements in the <code>display</code> list and turning it into a string:
  <pre><code>print(f"{' '.join(display)}")</code></pre></li>
  <li>We will also print the corresponding ASCII art for the number of lives remaining by accessing the appropriate element

<ol start="2">
  <li>Inside the game loop, we will print the corresponding ASCII art for the number of lives remaining by accessing the appropriate element in the <code>stages</code> attribute of the <code>hangman_art</code> module:
  <pre><code>print(hangman_art.stages[lives])</code></pre></li>
</ol>
<h2>Complete code</h2>
<p>Here is the complete code for the hangman game:</p>
<pre><code>#import the random module, hangman ascii art and words
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
        print(f" you entered {guess} and it's not in the word.")
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
    print(hangman_art.stages[lives])</code></pre>
    
    
# Conclusion
<p>In this tutorial, we learned how to create a simple hangman game in Python. We used loops, conditional statements, and various Python features to build the game and make it interactive</p>
