import socket
import os

TCPsock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
UDPsock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

while True:
 print(TCPsock.recvfrom(65565)) 