#!/usr/bin/env python
import socket, time, sys

def main():

	host = '127.0.0.1'
	port = 5001

	newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	newSocket.bind((host, port))
	
	newSocket.listen(1)

	conn, addr = newSocket.accept()
	print("Connection from {}".format(str(addr)))
	
	while True:
		data = conn.recv(1024).decode()
		if not data:
			break
		print("from connected user: {}".format(str(data)))
		data = str(data).upper()
		print("Received from user: {}".format(str(data)))
		data = input(" ? ")

	conn.send(data.encode())
	conn.close()

if __name__ == '__main__':
	main()
