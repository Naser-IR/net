import socket

import sys

ip = sys.argv[1]
port = sys.argv[2]
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
queue = []
while True:
	message = input("")
	if message == "5":
		while queue:
			print(queue.pop())
	else:
		
		s.sendto(message.encode(), (ip,int(port)))
		print("hh")
		
		try:
			data, addr = s.recvfrom(1024)
			queue.append(str(data)[2:])
		except:
			continue
