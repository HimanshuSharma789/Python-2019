import socket
# calling tcp socket
#s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# binding  ip and port 
s.bind(('localhost', 9990))
#  listen  number of consecutive connection 
s.listen(2)
#  re must accept connection from  client 
#  data variable --??client ip+port , client socket 
conn, addr = s.accept()
while True:
	print(addr, end=" @@  ")
	print(conn.recv(1000))
	print(">> ", end = "")
	conn.send(bytes(input(), 'utf-8'))
s.close()
