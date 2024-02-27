from socket import *
import time

# Server would be running on the same host as Client
serverName = ""
serverPort = 8085
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Set the socket timeout as 1 second
clientSocket.settimeout(1)

# Send 10 pings to the server
for sequence_number in range(1, 11):
    try:
        # Create message with the current sequence number and timestamp
        send_time = time.strftime("%H:%M:%S")
        message = f'Ping - sequence number: {sequence_number}, send time: {send_time}'

        # Record the start time and send the message
        start = time.time()
        clientSocket.sendto(message.encode(), (serverName, serverPort))

        # Receive the server's response
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        end = time.time()
        rtt = end - start

        # Print the server's response and the RTT
        print(f"Reply from server: {modifiedMessage.decode()}")
        print(f"RTT: {rtt:.5f} seconds\n")  # Format the RTT to 5 decimal places

    except timeout:
        # Print message if request times out
        print("Request timed out\n")

# Close the client socket
clientSocket.close()

