#!/usr/bin/env python
import json

PATH = "./sample_data.json"

if __name__ == '__main__':

    with open(PATH, 'r') as read_file:
        data = json.load(read_file)
    read_file.close()

    print(f"{type(data)}")

    for k, v in data.items():
        print(f"{k}:")
        for i in v:
            print(f"{i}")