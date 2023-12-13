from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    sentence = input('Client: ')
    clientSocket.send(sentence.encode('utf-8'))

    if sentence.lower() == 'bye':
        break

    response = clientSocket.recv(1024).decode('utf-8')
    print(f"Server: {response}")

clientSocket.close()
