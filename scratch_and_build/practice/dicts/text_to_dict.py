#!/usr/bin/env python
import sys

if __name__ == '__main__':

    if len(sys.argv) is not 2:
        print("[!] Usage {0} <text file>".format(sys.argv[0]))
        sys.exit(0)
    else:
        pass

    print("Args: {0}".format(len(sys.argv)))

    text_file_dict = dict()

    try:
        with open(sys.argv[1], 'r') as text_file:
            for index, line in enumerate(text_file):
                text_file_dict[index] = line
    except:
        print("[!] Something went wrong...")
    finally:
        text_file.close()

    for obj in text_file_dict.items():
        print(obj)

