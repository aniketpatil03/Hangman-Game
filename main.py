import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
 Death|
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Variable that is going to keep a track of lives
lives = 6

# Generating random word from list
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print("psst, the chosen random word", chosen_word)

# Generating as many blanks as the word
display = []
for _ in range(len(chosen_word)):
    display += "_"
print(display)

game_over = False

while not game_over:  # Condition for while loop to keep going
    # Taking input guess from user
    guess = input("Enter your guess: ").lower()

    # Replacing the blank value with guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if guess not in chosen_word:
        lives = lives - 1
        if lives == 0:
            print("The end, you lose")
            game_over = True

    if "_" not in display:
        game_over = True  # Condition which is required to end while loop or goes infinite
        print("Game Over, you won")

    # prints stages as per lives left from ASCII Art and art is arranged acc to it
    print(stages[lives])
