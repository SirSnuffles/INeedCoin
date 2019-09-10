import socket
import sys
from _thread import *

host = ""
port = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket Created!")

try:
	s.bind((host, port))
except socket.error:
	print("Bound Socket Error!")
	sys.exit()

print("Bound Socket Success!")

#backlog size, how many connections allowed
s.listen(10)

print("Socket ready")

def clientThread(conn):
	weclomeMessage = "Welcome to the server, type something and press Enter: \n"
	conn.send(weclomeMessage.encode())
	while True:
		data = conn.recv(1024)
		reply = "OK: " + data.decode()
		if not data:
			break
		print(reply)
		conn.sendall(data)

	conn.close()

while True:
	conn, addr = s.accept()

	print("Connect with client on IP: " + addr[0] + " port: " + str(addr[1]))

	start_new_thread(clientThread, (conn,))

print(data.decode())
s.close()