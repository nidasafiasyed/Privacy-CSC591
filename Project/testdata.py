import numpy
import csv
import time
from scapy.all import *
from scapy.utils import RawPcapReader
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, TCP
import pandas as pd
import os

def mapdevices():
    mapdev = {}
    df = pd.read_csv('device_mapping.csv')
    ipaddr = df[df.columns[1]]
    devname = df[df.columns[0]]
    for ip, dev in zip(ipaddr, devname):
        mapdev[ip] = dev
    return mapdev

def processpcap(files):
    #path = 'iot_traffic20180320/2018/03/20/'
    for filename in files:
    #filename = 'example.pcap'
    #pathtofile = path+filename
        packets = rdpcap(filename)
        for packet in packets:
            if packet.haslayer(TCP):
                checkpacket(packet)


def checkpacket(pkt):
    if IP in pkt:
        if pkt[IP].src in devmap or pkt[IP].dst in devmap:

            record=[]

            ipsrc = pkt[IP].src
            ipdst = pkt[IP].dst
            proto = 'TCP'
            lenpkt = len(pkt)
            timestamp = pkt.time
            local_time = time.localtime(timestamp)
            human_time = time.asctime(local_time)
            pkttime = time.strftime('%A, %d/%m/%y, %I:%M:%S %p', local_time)

            record.extend((ipsrc, ipdst, proto, lenpkt, pkttime))

            writer.writerow(record)

def datastream():

    with open('./datastreams/main.csv','r') as fd:
        data = csv.reader(fd)

        for row in data:
            for ip in devmap.keys():
                if ip in row:
                    with open('./datastreams/'+devmap[ip]+'.csv','a') as f:

                        datawriter = csv.writer(f)
                        datawriter.writerow(row)


if __name__== "__main__" :
#    files=[]
    '''path1 = './iot_traffic20180320/2018/03/20'
    for r,d,f in os.walk(path1):
        for filename in f:
            files.append(os.path.join(r, filename))
			
	
    path2 = './iot_traffic20180321/2018/03/21'
    for r,d,f in os.walk(path2):
        for filename in f:
            files.append(os.path.join(r, filename))
			
    path3 = './iot_traffic20180328/2018/03/28'
    for r,d,f in os.walk(path3):
        for filename in f:
            files.append(os.path.join(r, filename))
			
    path4 = './iot_traffic20180410/2018/04/10'
    for r,d,f in os.walk(path4):
        for filename in f:
            files.append(os.path.join(r, filename))
	
    path5 = './iot_traffic20180411/2018/04/11'
    for r,d,f in os.walk(path5):
        for filename in f:
            files.append(os.path.join(r, filename))
			
    path6 = './iot_traffic20180412/2018/04/12'
    for r,d,f in os.walk(path6):
        for filename in f:
            files.append(os.path.join(r, filename))
			
	path7 = './iot_traffic20180413/2018/04/13'
    for r,d,f in os.walk(path7):
        for filename in f:
            files.append(os.path.join(r, filename))
			
	path8 = './iot_traffic20180414/2018/04/14'
    for r,d,f in os.walk(path8):
        for filename in f:
            files.append(os.path.join(r, filename))
			
	path9 = './iot_traffic20180415/2018/04/15'
    for r,d,f in os.walk(path9):
        for filename in f:
            files.append(os.path.join(r, filename))
			
	path10 = './iot_traffic20180416/2018/04/16'
    for r,d,f in os.walk(path10):
        for filename in f:
            files.append(os.path.join(r, filename))
			
	path11 = './iot_traffic20180417/2018/04/17'
    for r,d,f in os.walk(path11):
        for filename in f:
            files.append(os.path.join(r, filename))
			
	path12 = './iot_traffic20180418/2018/04/18'
    for r,d,f in os.walk(path12):
        for filename in f:
            files.append(os.path.join(r, filename))
			
	path13 = './iot_traffic20180419/2018/04/19'
    for r,d,f in os.walk(path13):
        for filename in f:
            files.append(os.path.join(r, filename))'''
	
    files = ['eth1-20180320.0000.1521522000.pcap']
			
    devmap = {}

    devmap = mapdevices()

    fields = ['Source IP', 'Destination IP', 'Protocol', 'Bytes', 'Time']

    with open('./datastreams/main.csv','w') as fd:
        writer = csv.writer(fd)
        writer.writerow(fields)

        processpcap(files)

    datastream()
