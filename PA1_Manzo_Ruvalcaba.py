from socket import *
import time

serverName = 'SpiritBreaker'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1); # sets the timeout to 1 second
#round_trip_time = 0
sequence_number = 1

while True:
    start= time.time()
    message = "PING: " + str(sequence_number) + " " + str(send_start)
    clientSocket.sendto(message.encode(),(serverName, serverPort))

    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        elapsed = time.time() - start
        round_trip_time += time.time() - elapsed #elapsed time
        print (modifiedMessage.decode())
        print "Round Trip Time is:" + str(elapsed) + " seconds"
    except socket.timeout: #if no reply within 1 second
        print (modifiedMessage.decode())
        print ('Request timed out')

    if sequence_number > 10
        break
clientSocket.close()
