#!/usr/bin/env python
# HW04_ch07_ex02

# The built-in function eval takes a string and evaluates it using the Python
# interpreter.
# For example:

#     >>> eval('1 + 2 * 3')
#     7
#     >>> import math
#     >>> eval('math.sqrt(5)')
#     2.2360679774997898
#     >>> eval('type(math.pi)')
#     <type 'float'>

# Write a function called eval_loop that iteratively prompts the user, takes
# the resulting input and evaluates it using eval, and prints the result.

# It should continue until the user enters 'done', and then return the value of
# the last expression it evaluated.

###############################################################################
# Imports
import math

# Body
def eval_loop():
	# define the output
	output = "Nothing to Evaluate"

	while True:
		# prompt for user input
		usrInput = input("Enter An Input: ")
		if(usrInput == 'done'):
			print("Eval =", output)
			break
		else:
			output = eval(usrInput)
			print("Eval =", output)

###############################################################################
def main():
    pass  # Remove this line and uncomment below once eval_loop is defined.
    eval_loop()

if __name__ == '__main__':
    main()
