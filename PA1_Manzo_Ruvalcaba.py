from socket import *
import time

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1); # sets the timeout to 1 second
round_trip_times = [] #an array that stores all the round trip times
sequence_number = 1
packets_lost = 0
smallRTT = 100
largeRTT = -1
avergRTT = 0
################################################################################
print ("-------------------------------------------------")
while True:
    start= time.time() #keeps the start of the ping
    message = "PING: " + str(sequence_number) + " " + str(round(start, 3))
    clientSocket.sendto(message.encode(),(serverName, serverPort)) #sends the message to the server
    try: # if there is a response from the server
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        elapsed = time.time() - start #calculates the time elapsed from message sent and message recieved
        round_trip_times.append(elapsed) #elapsed times or RTT's in an array
        print (modifiedMessage.decode())
        print ("Round Trip Time is:" + str(round(elapsed,3)) + " seconds")
        print ("-------------------------------------------------")
    except timeout: #if no reply within 1 second
        print (message)
        print ("Request timed out")
        print ("-------------------------------------------------")
        packets_lost = packets_lost + 1 #keeps track of lost packets
    sequence_number += 1
    if sequence_number > 10: #stops sendind pings after 10 messages
        break
################################################################################
round_trip_times.sort()
for x in round_trip_times: # finds min, max, and calculates average RTT's
    if x > largeRTT:
        largeRTT = x
    if x < smallRTT:
        smallRTT = x
    avergRTT = avergRTT + x
################################################################################
print ("")
avergRTT = avergRTT / len(round_trip_times)
# prints out all extra credit information
print ("Maximum RTT: " + str(round(largeRTT, 4)) + " seconds")
print ("Minimum RTT: " + str(round(smallRTT, 4)) + " seconds")
print ("Average RTT: " + str(round(avergRTT, 4)) + " seconds")
if packets_lost == 0: # if no packets lost (avoids calculation error)
    print ("Packet loss percentage: 0%")
else: # prints out the packet loss percentage
    print ("Packet loss percentage: " + str((packets_lost/10) * 100) + "%")
clientSocket.close()
