# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 5 for the task.
# Please do provide function calls that test/demonstrate your
# function.

def rotate_word(strEncode, intRotate):
	# initialise the output variable
	output = ''

	# check if the intRotate is negative, if yes then convert it to positive by taking the mod
	if(intRotate < 0):
		intRotate = intRotate % 26

	# loop through the entire string and populate the output variable by appending the rotated characters
	for strCharacter in strEncode:
		if(ord(strCharacter) >= 65 and ord(strCharacter) <= 90):
			output += chr(65 + ((ord(strCharacter) + intRotate) % 65) % 26)
		elif(ord(strCharacter) >= 97 and ord(strCharacter) <= 122):
			output += chr(97 + ((ord(strCharacter) + intRotate) % 97) % 26)
		else:
			output += strCharacter

	return output

def main():

	print("The program will ask you to input a String to encrypt and a number to rotate the string. To end, type an empty string\n")
	while True:
		usrInput = input("Enter A String To Encrypt: ")
		if(usrInput == ''):
			break
		numRotate = int(input("Enter A Number: "))

		print("The Encrypted String Is:", rotate_word(usrInput, numRotate) + "\n")

if __name__ == '__main__':
	main()