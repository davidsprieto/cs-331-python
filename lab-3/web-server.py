# import socket module
from socket import *

# In order to terminate the program
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
HOST = ""
PORT = 8085
serverSocket.bind((HOST, PORT))
serverSocket.listen()

print(f"The server is ready to receive on port: {PORT}")

while True:
    # Establish the connection
    connectionSocket, addr = serverSocket.accept()
    print('Ready to serve...')
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        output_data = f.read()
        f.close()
        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        # Send the content of the requested file to the client
        for i in range(0, len(output_data)):
            connectionSocket.send(output_data[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        header = "HTTP/1.1 404 Not Found\nContent-Type: text/html\n\n"
        connectionSocket.send(header.encode())
        error_message = "<html><head><meta charset='UTF-8'><title>Socket Programming // Hello World</title></head><body><h1>404 Not Found</h1></body></html>"
        connectionSocket.send(error_message.encode())
        # Close client socket
        connectionSocket.close()
        break
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
