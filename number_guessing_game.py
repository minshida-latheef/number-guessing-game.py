import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Count the number of attempts
attempts = 0

print("🎯 Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100.")
print("Can you guess it?")

# Keep asking until the player guesses correctly
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
        break