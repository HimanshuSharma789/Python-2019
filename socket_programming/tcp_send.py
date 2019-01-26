import socket
# calling tcp socket
#s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#  if  rec started  listening then we can connect
s.connect(('localhost', 9990))
while True:
	print(">> ", end="")
	s.send(bytes(input(), 'utf-8'))
	print(s.recv(1000))
socket.close()
