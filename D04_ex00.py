#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import random

# Body
def guessNumber():
	# create a random number
	randNum = random.randint(1, 25)

	# initialise the number of tries the user can have. Max 5 Tries
	nGuess = 0

	while nGuess < 5:
		
		try:
			# take an input from the user and check if it is a valid integer			
			usrInput = int(input("\nEnter A Number: "))
			nGuess += 1
		except ValueError:
			# catch ValueError and tell the user to input a valid integer
			print("Input Error: Enter A Valid Number")
			nGuess += 1
			continue
		
		if(usrInput == randNum):
			print("Awesome! You Guessed The Right Number. (Number Of Tries: " + str(nGuess) + ")")
			return
		elif(usrInput < randNum):
			print("Too Low. Try Again!")
		elif(usrInput > randNum):
			print("Too High. Try Again!")

	print("\nSorry! You Have Exhausted Your 5 Attempts. The Actual Number Was: " + str(randNum))


################################################################################
def main():
    
	guessNumber()

if __name__ == '__main__':
    main()