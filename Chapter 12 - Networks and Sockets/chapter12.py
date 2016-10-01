#!/usr/bin/python

# Chapter 12 Assignment: Understanding the Request / Response Cycle

# Exploring the HyperText Transport Protocol

# You are to retrieve the following document using the HTTP protocol in a way
# that you can examine the HTTP Response headers.

# http://data.pr4e.org/intro-short.txt
# There are three ways that you might retrieve this web page and look at the
# response headers:

# Preferred: Modify the socket1.py program to retrieve the above URL and print
# out the headers and data. Make sure to change the code to retrieve the above
# URL - the values are different for each URL.

# Open the URL in a web browser with a developer console or FireBug and manually
# examine the headers that are returned.

# Use the telnet program as shown in lecture to retrieve the headers and content.

import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('www.pythonlearn.com', 80))

mysocket.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.1\r\nHost: www.pythonlearn.com\r\n\r\n')

while True:
    data = mysocket.recv(512)
    if (len(data) < 1):
        break
    print data

mysocket.close()
