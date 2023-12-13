from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('localhost', serverPort))
print("The server is ready to receive")

while True:
    sentence, clientAddress = serverSocket.recvfrom(1024)
    sentence = sentence.decode('utf-8')

    print(f"Client ({clientAddress}): {sentence}")

    response = input('Server: ')
    serverSocket.sendto(response.encode('utf-8'), clientAddress)
