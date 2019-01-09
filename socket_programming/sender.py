#!/usr/bin/env python3
import socket

ip = '127.0.0.1'
port = 9090

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = bytes(input("type your message: "), 'utf-8')
    s.sendto(data, (ip, port))
