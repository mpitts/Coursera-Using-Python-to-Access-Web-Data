#!/usr/bin/python

# Chapter 3 examples using either the socket library or the urllib library to read a URL.

import socket
import urllib

# socket library example:

print 'Output from the socket library example:\n'

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('www.py4inf.com', 80))

mysocket.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
    data = mysocket.recv(512)
    if (len(data) < 1):
        break
    print data

mysocket.close()

# urllib library example:

print '\n\nOutput from the urllib library example:\n'

myurl = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

for line in myurl:
    print line.rstrip()
