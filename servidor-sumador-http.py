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

        _, op1, operando, op2 = resource.split('/')

        number1 = int(op1)
        number2 = int(op2)

        html_response = calculadora.operaciones[operando](number1, number2)

        recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                              '<html><h1>Sumador Simple</h1>' +
                              str(html_response) +
                              '\r\n', 'utf-8'))
        recvSocket.close()

except KeyboardInterrupt:
    print('Closing binding sockets')
    mySocket.close()
