from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()

    while True:
        sentence = connectionSocket.recv(1024).decode('utf-8')
        if not sentence:
            break

        print(f"Client: {sentence}")

        response = input('Server: ')
        connectionSocket.send(response.encode('utf-8'))

    connectionSocket.close()
