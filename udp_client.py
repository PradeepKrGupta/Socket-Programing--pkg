from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    sentence = input('Client: ')
    clientSocket.sendto(sentence.encode('utf-8'), (serverName, serverPort))

    if sentence.lower() == 'bye':
        break

    response, serverAddress = clientSocket.recvfrom(1024)
    response = response.decode('utf-8')
    print(f"Server ({serverAddress}): {response}")

clientSocket.close()
