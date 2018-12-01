#!/usr/bin/env python
import os, time, sys

def main():

    os.system('clear')
    time.sleep(1)

    while True:
        
        name = input('Please enter your name: ')
        age = int(input('How old are you?: '))
        
        if age >= 18 and age <= 30:
            print('{}, you meet the age requirements...'.format(name))
        elif age == 0:
            print('Now exiting...')
            break
        else:
            print('{}, you do not meet the age requireents...'.format(name))


if __name__ == '__main__':
    main()