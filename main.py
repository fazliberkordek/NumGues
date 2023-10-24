# @author: fazliberkordek
# @date: 2023-10-25
# @description: Main file for the project.

import random
import math

# Taking inputs from user
print("Welcome to the game!")
lower = int(input("Enter the Lower bond: -")) # The lower bond is the min of the range
upper = int(input("Enter the Upper Bond"))# The upper bond is the max num of the range

#Creating the range of the bounds

bound = random.randint(lower,upper)
x = math.log(upper-lower+1,2)
print("\n you've only",
      round(x),
      "chances to guess the integer\n")
#Initializing the guessing:

guess_count = 0
#for calculation of the minumun number of
# guess depends upon range
while(guess_count<x):
    guess_count+=1

    #taking guessing number
    guess_num = int(input("Guess a number: -"))
    if bound ==guess_num:
        print("Congrats")
        break
    elif bound>guess_num:
        print("You guessed too small")
    elif bound<guess_num:
        print("You guessed too high")

if guess_count >= x:
    print("\nThe number is %d" %guess_count)
    print("\nBetter luck next time ")





