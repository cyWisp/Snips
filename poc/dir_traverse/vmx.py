#!/usr/bin/env python
import os

def get_vmx_files(path):
	vmx_files = dict()
	for root, dirs, files in os.walk(path):
		for name in files:
			if name[-3:] == "vmx": 
				vmx_files[name[:-4]] = os.path.join(root, name)

	return vmx_files
