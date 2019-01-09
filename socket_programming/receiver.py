#!/usr/bin/env python3
import socket

ip = "127.0.0.1"
port = 9090

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((ip, port))

while True:
    print(s.recvfrom(100))
