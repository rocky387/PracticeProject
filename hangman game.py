import random

# List of words to choose from
words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']

# Choose a random word from the list
secret_word = random.choice(words)

# Initialize variables
guesses = []
max_guesses = 6

# Loop until the player runs out of guesses or guesses the word
while len(guesses) < max_guesses and not all(letter in guesses for letter in secret_word):
    # Print the current state of the game
    print('Current word:', ''.join(letter if letter in guesses else '_' for letter in secret_word))
    print('Guesses:', guesses)
    print('Remaining guesses:', max_guesses - len(guesses))

    # Get the player's guess
    guess = input('Enter a letter: ')

    # Validate the guess
    if len(guess) != 1:
        print('Please enter a single letter.')
    elif not guess.isalpha():
        print('Please enter a letter.')
    elif guess in guesses:
        print('You have already guessed that letter.')
    else:
        # Add the guess to the list of guesses
        guesses.append(guess)

        # Check if the guess is correct
        if guess in secret_word:
            print('Correct!')
        else:
            print('Incorrect!')

# Print the final state of the game
if all(letter in guesses for letter in secret_word):
    print('Congratulations, you won! The word was', secret_word)
else:
    print('Sorry, you lost. The word was', secret_word)
