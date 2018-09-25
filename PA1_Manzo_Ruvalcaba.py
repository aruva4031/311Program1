from socket import *
import time
serverName = 'SpiritBreaker'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = "ping"
round_trip_time = 0
send_start = 0
data_received = 0
clientSocket.settimeout(1.00)

for x in 10:
    send_start= time.time()
    clientSocket.sendto(message.encode(),(serverName, serverPort))

    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print (modifiedMessage.decode())
        
clientSocket.close()
