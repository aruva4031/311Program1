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
largeRTT = -1
avergRTT = 0
################################################################################
print ("-------------------------------------------------")
while True:
    start= time.time()
    message = "PING: " + str(sequence_number) + " " + str(round(start, 3))
    clientSocket.sendto(message.encode(),(serverName, serverPort))
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        elapsed = time.time() - start
        round_trip_times.append(elapsed) #elapsed time
        print (modifiedMessage.decode())
        print ("Round Trip Time is:" + str(round(elapsed,3)) + " seconds")
        print ("-------------------------------------------------")
    except timeout: #if no reply within 1 second
        print (message)
        print ("Request timed out")
        print ("-------------------------------------------------")
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
    avergRTT = avergRTT + x
################################################################################
print ("")
avergRTT = avergRTT / len(round_trip_times)
print ("Maximum RTT: " + str(round(largeRTT, 4)) + " seconds")
print ("Minimum RTT: " + str(round(smallRTT, 4)) + " seconds")
print ("Average RTT: " + str(round(avergRTT, 4)) + " seconds")
if packets_lost == 0:
    print ("Packet loss percentage: 0%")
else:
    print ("Packet loss percentage: " + str((packets_lost/10) * 100) + "%")
clientSocket.close()
