#!/usr/bin/env python
import os

if __name__ == '__main__':

	for k, v in os.environ.items():
		print(f"{k}: {v}")
