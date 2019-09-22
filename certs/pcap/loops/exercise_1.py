#!/usr/bin/env python

if __name__ == '__main__':

	# Create a for loop that counts from 0 to 10, and prints odd numbers to the screen.
	
	for i in range(1, 11, 2):
		print(i)

	# or

	for i in range(1, 11):
		if i % 2 != 0:
			print(i)
