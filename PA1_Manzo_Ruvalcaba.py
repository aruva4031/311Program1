from socket import *
import time

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1); # sets the timeout to 1 second
round_trip_times = []
sequence_number = 1
packets_lost = 0
smallRTT = 100
largeRTT = 0
averageRTT = 0
################################################################################
while True:
    start= time.time()
    message = "PING: " + str(sequence_number) + " " + str(round(start, 3))
    clientSocket.sendto(message.encode(),(serverName, serverPort))
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        elapsed = time.time() - start
        round_trip_times.append(time.time() - elapsed) #elapsed time
        print (modifiedMessage.decode())
        print ("Round Trip Time is:" + str(round(elapsed,3)) + " seconds")
    except socket.timeout: #if no reply within 1 second
        print (message)
        print ("Request timed out")
        packets_lost = packets_lost + 1
    sequence_number += 1
    if sequence_number > 10:
        break
################################################################################
round_trip_times.sort()
for x in round_trip_times:
    if x > largeRTT:
        largeRTT = x
    if x < smallRTT:
        smallRTT = x
    averageRTT = AverageRTT + x
################################################################################
averageRTT = averageRTT / len(round_trip_times)
print ("Maximum RTT: " + largeRTT + " seconds")
print ("Minimum RTT: " + smallRTT + " seconds")
print ("Average RTT: " + averageRTT + " seconds")
print ("Packet loss percentage: " + (packets_lost/10) * 100 + "%")
clientSocket.close()
