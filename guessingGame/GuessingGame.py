import random # We are going to need this package to generate a random number

def guessingGame():
    # Generate a random number between 1 and 100
    secretNumber = random.randint(1, 100)
    
    guess = None

    # Continue looping until the user guesses correctly
    while guess != secretNumber:
        guessInput = input("Enter your guess: ")

        # Check if the input is made up of only digits
        if not guessInput.strip().isdigit():
            print("Please enter a valid integer.")
            continue # This returns to the loop header to ask again.

        guess = int(guessInput) # Converts the string made up of digits to an int type

        # Provide hints based on the guess
        if guess < secretNumber:
            print("Too low! Try again.")
        elif guess > secretNumber:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number!")

# Start the game
guessingGame()