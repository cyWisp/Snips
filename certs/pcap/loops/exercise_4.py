#!/usr/bin/env python

if __name__ == '__main__':

	# Create a program with a for loop and a continue statement. The program should iterate
	# over a string of digits, replace each 0 with x, and print the modified string to the
	# screen.

	for digit in "0165031806510":
		if digit == "0":
			print("x", end="")
			continue
		print(digit, end="")
