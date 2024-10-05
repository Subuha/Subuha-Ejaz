import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the correct number to win.\n")

    level = 1
    score = 0
    
    while True:
        print(f"\nLevel {level}")
        max_number = 10 * level  # Increase the range with each level
        secret_number = random.randint(1, max_number)
        attempts = 5 - level // 2  # Decrease attempts as the level increases
        
        if attempts < 1:
            attempts = 1  # Minimum of 1 attempt
        
        print(f"Guess the number between 1 and {max_number}. You have {attempts} attempts.")

        for i in range(attempts):
            guess = int(input(f"Attempt {i + 1}/{attempts}: Enter your guess: "))
            
            if guess == secret_number:
                print("Congratulations! You guessed it right.")
                score += 1
                break
            elif guess < secret_number:
                print("Too low!")
            else:
                print("Too high!")
        
        if guess != secret_number:
            print(f"Sorry, you've used all attempts. The correct number was {secret_number}.")
            break

        # Progress to the next level
        level += 1

    print(f"\nGame over! You reached level {level} with a score of {score}.")

# Start the game
number_guessing_game()
