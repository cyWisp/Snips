#!/usr/bin/env python
import socket, sys

#socket creation and instantiation
#practice writing this function 3 times a day
def create_socket():

	try:
		global host
		global port
		global conSocket

		host = ""
		port = 9999
		conSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error as error_msg:
		print("Socket Creation Failed!\n Error Code: {} Error Message: {}".format(error_msg[0], str(error_msg[1])))
	finally:
		print("success!!!")

#-------------------------------------------------------------------------------------

def bind_socket():

	try:
		global host
		global port
		global conSocket

		conSocket.bind((host, port))
		conSocket.listen(5)

		print("[*] Binding host to port {}".format(str(port)))
		
	except socket.error as error_message:
		print("Port bind error!\nError Message {} Error Code {}\n retrying...".format(error_message[0], str(error_message[1])))

		#recursion
		bind_socket()

	finally:
		print("Socket creation successful!")
def main():

	create_socket()
	bind_socket()

if __name__ == '__main__':
	main()
