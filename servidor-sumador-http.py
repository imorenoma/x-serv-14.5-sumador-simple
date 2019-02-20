#!/usr/bin/python3

import socket
import random
import calculadora

PORT = 1234

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

mySocket.bind((socket.gethostname(), 1234))

mySocket.listen(20)

try:
    while True:

        print('Waiting for connections ...')

        (recvSocket, address) = mySocket.accept()
        print('Request received:')

        request = str(recvSocket.recv(2048), 'utf-8')
        print(request)

        resource = request.split()[1]
        print(resource)

        recvSocket.close()
except KeyboardInterrupt:
    print('Closing binding sockets')
    mySocket.close()



