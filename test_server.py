from socket import *
import struct

serverName = 'localhost'
serverPort = 12000

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)
print('Connected with client:')

connectionSocket, clientAddr = serverSocket.accept()
Values = connectionSocket.recv(8)
val1,val2 = struct.unpack('!ii',Values)
print(f"value1 and value2 recived from Client is {val1} , {val2}")

sumRes = val1+val2
print(f"sum send to client is {sumRes}")
connectionSocket.send(struct.pack('!i',sumRes))

serverSocket.close()


