# while loop makes a section of code repeat until a certain condition is met. 
# You will create a Python script that asks the user to correctly guess a number
import random
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
# Next, enter a statement that will generate a random number between 1 and 10 by using the randint() function of the random module.
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    # The while loop will repeat the code inside the loop until the number is guessed correctly, 
    # which is represented by the condition isGuessRight != True in the code.
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
# If the user has not guessed the correct answer, enter the loop.
# Ask the user for a guess.
# Is the guess the correct number?
# If the correct guess, tell the user it was the correct guess and exit the loop.
# If the wrong guess, tell the user it was the wrong guess and continue the loop.