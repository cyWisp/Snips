#!/usr/bin/env python
import os, sys

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("[!] Usage: args.py [arg_1] [arg_2]")
        sys.exit(1)
    else:
        pass
    
    if isinstance(sys.argv[1], int) and isinstance(sys.argv[2], int):
        pass
    else:
        print("[x] Please enter two integers...")
        sys.exit(1)

    print("The sum is " + str(sum(sys.argv[1], sys.argv[2])))

    
       
     

    
