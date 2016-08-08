#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises


# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.

# Imports
import math

def verbing(s):
    
    output = ''

    # calculate the length of the string
    strLength = len(s)
    if(strLength < 3):
        output = s
    else:
        if(s[-3:].lower() == 'ing'):
            output = s + 'ly'
        else:
            output = s + 'ing'

    return output


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):

    output = ''

    # Get the index of the first appearance of 'not'
    indexNot = s.lower().find('not')

    # Get the index of the first appearance of 'bad'
    indexBad = s.lower().find('bad')

    if(indexNot > indexBad):
        output = s
    else:
        output = s[:indexNot] + "good" + s[indexBad + 3:]
    
    return output


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
    
    # declare variables
    front_A = ''
    front_B = ''
    back_A = ''
    back_B = ''
    index = 0

    length_A = len(a)
    length_B = len(b)

    if(length_A % 2 == 0):
        index = int(length_A / 2)
        front_A = a[:index]
        back_A = a[index:]
    else:
        index = int(math.floor(length_A / 2))
        front_A = a[:index + 1]
        back_A = a[index + 1:]

    if(length_B % 2 == 0):
        index = int(length_B / 2)
        front_B = b[:index]
        back_B = b[index:]
    else:
        index = int(math.floor(length_B / 2))
        front_B = b[:index + 1]
        back_B = b[index + 1:]

    return (front_A + front_B + back_A + back_B)


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
    main()
