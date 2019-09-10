import socket
import sys

try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

except socket.error:
	print("Failed to connect")
	sys.exit()

print("Socket Created!")

host = "www.google.com"
port = 80

try:
	remote_ip = socket.gethostbyname(host)

except socket.geterror:
	print("Host name could not be found!")
	sys.exit()
# print(remote_ip, type(remote_ip))
remote_ip = "8888"
# port = 46646

# end()

print("IP_address: " + remote_ip)

s.connect((remote_ip, port))

print("Socket connected to " + host + " using IP: " + remote_ip)

message = "GET / HTTP/1.1\r\n\r\n"

try:
	s.sendall(message.encode())

except socket.error:
	print("Did not send correctly")

print("message sent successfully")

reply = s.recv(4096)
# print('received reply?')

print(reply.decode())

s.close()