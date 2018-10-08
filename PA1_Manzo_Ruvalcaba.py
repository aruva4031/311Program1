from socket import *
import time

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1); # sets the timeout to 1 second
round_trip_times = [] #an array that stores all the round trip times
sequence_number = 1
avergRTT = 0
packets_lost = 0
################################################################################
print ("-------------------------------------------------")
while True:
    start= time.time() #keeps the start of the ping
    message = "PING: " + str(sequence_number) + " " + str(round(start, 3)) #time is measured since epoch (1 January, 12:00 am, 1970)
    clientSocket.sendto(message.encode(),(serverName, serverPort)) #sends the message to the server
    try: # if there is a response from the server
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        elapsed = time.time() - start #calculates the time elapsed from message sent and message recieved
        round_trip_times.append(elapsed) #elapsed times or RTT's in an array
        print (message)
        print ("Round Trip Time is:" + str(elapsed) + " seconds")
        print ("-------------------------------------------------")
    except timeout: #if no reply within 1 second
        print (message)
        print ("Request timed out")
        print ("-------------------------------------------------")
        packets_lost += 1 #keeps track of lost packets
    sequence_number += 1
    if sequence_number > 10: #stops sendind pings after 10 messages
        break

################################################################################
print ("")
avergRTT = sum(round_trip_times, 0.0) / len(round_trip_times)
# prints out all extra credit information
print ("Maximum RTT: " + str(max(round_trip_times)) + " seconds")
print ("Minimum RTT: " + str(min(round_trip_times)) + " seconds")
print ("Average RTT: " + str(avergRTT) + " seconds")
if packets_lost == 0: # if no packets lost (avoids calculation error)
    print ("Packet loss percentage: 0%")
else: # prints out the packet loss percentage
    print ("Packet loss percentage: " + str(packets_lost * 10) + "%")
clientSocket.close()
