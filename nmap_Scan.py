#!/usr/bin/python3

import nmap
import pyfiglet

# Function to display a banner using Figlet
def display_banner():
    banner = pyfiglet.figlet_format("Nmap Scanner", font="slant")
    print(banner)
    print("<------------------------------------------------------------------>")
    print("Welcome to the Nmap Automation Tool")
    print("<------------------------------------------------------------------>")

# Display the banner
display_banner()

scanner = nmap.PortScanner()

ip_address = input("Enter IP address you want to scan: ")
print("The IP address you entered: ", ip_address)

res = input('''Please select the type of scan:
            1) SYN ACK Scan
            2) UDP Scan
            3) Comprehensive Scan
            Enter your choice (1-3): ''')
print("You have selected the option: ", res)

if int(res) == 1:
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("IP status:", scanner[ip_address].state())
    print("Protocols:", scanner[ip_address].all_protocols())
    print("Open ports:", scanner[ip_address]['tcp'].keys())

elif int(res) == 2:
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("IP status:", scanner[ip_address].state())
    print("Protocols:", scanner[ip_address].all_protocols())
    print("Open ports:", scanner[ip_address]['udp'].keys())

elif int(res) == 3:
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sV -sC -O -sS')
    print(scanner.scaninfo())
    print("IP status:", scanner[ip_address].state())
    print("Protocols:", scanner[ip_address].all_protocols())
    print("Open ports:", scanner[ip_address]['tcp'].keys())

else:
    print('Please enter a valid option for the scan.')

    