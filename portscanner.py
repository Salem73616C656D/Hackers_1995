#! /usr/bin/env python3
# Script Name:      portscanner
# Author:           marburgja
# Last Rev:         20211206
# Purpose:          scan for port availability with socket library
# Reference:        https://www.geeksforgeeks.org/port-scanner-using-python/
#                   https://codefellows.github.io/ops-401-cybersecurity-guide/curriculum/class-44/challenges/DEMO.html


import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 5
sockmod.settimeout(timeout) #setting timeout for the scan

hostip = input("Enter IP To Scan:")
portno = input("Enter Port Number:")

def portScanner(hostip,portno):
    if sockmod.connect_ex((hostip, int(portno))): #tests connecting to address:port
        print("Port Closed")  #if connection times out returns closed
    else:
        print("Port Open")  #if it connects returns open

portScanner(hostip,portno)