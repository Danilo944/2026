import random

random_number = random.randint(1, 10)

print("Guess a number between 1 and 10.")

while True:
    user_guess = input("Enter your guess: ")
    user_guess = int(user_guess)
    # To do: Add a conditional to check the user's guess.
    #        If the guess is too high, print "Too high!".
    if user_guess > random_number:
        print("Too high")
    elif user_guess < random_number:
        print("Too low")
    else:
        print("Correct! You guessed the number")




    #        If the guess is too low, print "Too low!"
    #        If the guess is correct, print "Correct! You guessed the number!" and stop the game.