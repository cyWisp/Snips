#!/usr/bin/env python
from ftplib import FTP

def place_file(ftp_object):

    file_name = 'test.txt'
    ftp_object.storbinary('STOR' + file_name, open(file_name, 'rb'))

if __name__ == '__main__':

    # define url, creds, establish connection and log in
    creds = ('domain', 'username', 'password')
    ftp = FTP(creds[0])
    ftp.login(user=creds[1], passwd=creds[2])

    # change current working directory before upload
    # and show contents
    ftp.cwd('/public_html/')
    #ftp.dir()
    
    # upload 'test.txt'
    place_file(ftp)

    # show contents to prove file has been uploaded
    ftp.dir()
    ftp.quit()


    





