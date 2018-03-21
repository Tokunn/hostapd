#!/usr/bin/env python2

import socket

TCP_IP = "0.0.0.0"
TCP_PORT = 8001
BUFFER_SIZE = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(10)

while 1:
    conn, addr = s.accept()
    print "Connection address:", addr
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        print "received data:", data
        conn.send(data)
conn.close()
