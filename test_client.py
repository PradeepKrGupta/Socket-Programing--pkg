from socket import *
import struct

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

val1 = int(input('Enter val1 :'))
val2 = int(input('Enter val2 :'))

values = struct.pack('!ii',val1,val2)
clientSocket.sendall(values)

resVal = clientSocket.recv(4)
sumVal = struct.unpack('!i',resVal)[0]

mean = sumVal/2
print(f"Sum Value is :{sumVal}")
print(f"Mean Value is :{mean}")

