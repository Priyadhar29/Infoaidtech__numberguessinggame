#Let's create a simple program to guess the number

import random

print('Welcome to GUESS ME! ')
print('I am thinking of a number between 1 to 10')
print("Can you guess the number")
print("LET'S PLAY!")

num = random.randint(1,10)

guess = int(input("Guess a number between 1 and 10:"))

while guess != num:
    
    if guess > num:
        print("Your guess is too high.")

    elif guess < num:
        print("Your guess is too low.")

    guess = int(input("Guess again:"))
print("Congratulations! You guessed it correctly.")
