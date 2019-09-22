#!/usr/bin/env python

if __name__ == '__main__':
	
	# Create a program with a for loop an a break statement. The program should iterate over characters in an email address, exit the loop when it reaches the @ symbol, and print the part before @ on one line.

	for ch in "rob@gmail.com":
		if ch == "@":
			break
		print(ch, end="")
