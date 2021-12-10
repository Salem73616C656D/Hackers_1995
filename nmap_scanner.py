#! /usr/bin/env python3
# Script Name:      nmap
# Author:           marburgja
# Last Rev:         20211202
# Purpose:          perform nmap functionality
# Reference:        https://www.pythonpool.com/python-nmap/


# Libraries
import nmap

# Variables
scanner = nmap.PortScanner()

# Functions
def synack():
    ip_addr = input("Enter IP Address To Scan:")
    range = input("Enter Port Range (i.e. 1-50):")
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

def udp():
    ip_addr = input("Enter IP Address To Scan:")
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    # state() tells if target is up or down
    print("Ip Status: ", scanner[ip_addr].state())
    # all_protocols() tells which protocols are enabled like TCP UDP etc
    print("protocols:",scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())

def compscan():
    ip_addr = input("Enter IP Address To Scan:")
    print("Nmap Version: ", scanner.nmap_version())
    # sS for SYN scan, sv probe open ports to determine what service and version they are running on
    # O determine OS type, A tells Nmap to make an effort in identifying the target OS
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

def main():
    while True:
        print("Nmap Automation Tool")
        print("--------------------")

        resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) Comprehensive Scan             
                4) Exit \n""")
        
        if resp == "1":
            synack()
        if resp == "2":
            udp()
        if resp == "3":
            compscan()
        if resp == "4":
            break

# Main
main()