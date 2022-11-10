import socket
import sys

port = sys.argv[1]
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('',int(port)))
names = {}

while True:
	data,addr = s.recvfrom(1024)

	data_string = str(data)
	if data_string[2] == "1":
		names[addr] = data_string[4:]
		s1 = names[addr] + " has joined"
		for key in names.keys():
			if(key != addr):
				s.sendto(s1.encode(),key)
		print(names)
	if data_string[2] == "2":
		s1 = names[addr] + data_string[4:]
		for key in names.keys():
			if(key != addr):
				s.sendto(s1.encode(),key)
	if data_string[2] == "3":
		s1 = names[addr] +" changed his name to " +data_string[4:]
		names[addr] = data_string[4:]
		for key in names.keys():
			if(key != addr):
				s.sendto(s1.encode(),key)
		
	if data_string[3] == "4":
		s1 = names[addr] + " has left the group"
		for key in names.keys():
			if(key != addr):
				s.sendto(s1.encode(),key)
		
		
		
		
