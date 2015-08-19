import os
import re
import time
import sys
import math
import random
import subprocess
 
startTime = time.time()
endTime = time.time()
def nextTime(rateParameter):
    return -math.log(1.0 - random.random()) / rateParameter

#def sendPackets(numberOfPackets, rateParameter):
def sendPackets(numberOfPackets):

    #meanInterval=[2,1.5,1,0.5,0.2,0.1,0.05,0.01,0.001]
    meanInterval=[0.001]    
    listSize= len(meanInterval)
    for i in range(0,listSize):
        meanI=meanInterval[i]
        fileOpen1 = open("PingResult_H2_H5_SNw_" + str(numberOfPackets)+ "pkt_I" + str(meanI) + "s_3.csv", 'a')
        for n in range(numberOfPackets): # start ping processes
            waitingTime = nextTime(1/(meanI*1.0))
            ip = "10.0.0.5"
            global startTime 
            startTime = time.time()
            PingFile = subprocess.Popen(["ping", "-c 1", "-q", ip], stdout=subprocess.PIPE)
            pingRes,pingErr = PingFile.communicate()
            fileOpen1.write(str(time.time())+ '\t' + pingRes + '\n')
            time.sleep(waitingTime)
        fileOpen1.close()
        
#PktSize =[1000,500,200,100]
numPkt = [100]
lenNumPkt = len(numPkt)
for pkt in range(0,lenNumPkt):
    numPkt = numPkt[pkt]
    sendPackets(numPkt)  #  number of packet sent passed as an argument
    endTime = time.time()
    totalTime = endTime - startTime 