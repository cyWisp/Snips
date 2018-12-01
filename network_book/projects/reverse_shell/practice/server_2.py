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
		print("Socket Creation Failed! Error Code: {} Error Message: {}".format(error_message[0], str(error_message[1])))
	finally:
		print("Socket Creation Successful!")

def bind_socket():

	try:
		global host
		global port
		global conSocket

		conSocket.bind((host, port))
		conSocket.listen(5)
		
		print("binding host to port {}".format(str(port)))
	except socket.error as err_msg:
		print("Socket bind error!\nError Code: {} Error Message: {}\nRetrying...".format(err_msg[0], str(err_msg[1])))
	finally:
		print("socket bind succeeded!!!")


def main():

	create_socket()
	bind_socket()

if __name__=='__main__':
	main()
