#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
import cv2
import numpy

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
#host = 'RASPBERRYPI'
port = 12345                # Reserve a port for your service.

print host

s.connect((host, port))
data = s.recv(1024000)
s.close                     # Close the socket when done

frame = numpy.fromstring(data, dtype=numpy.uint8)
frame = numpy.reshape(frame, (480,640,3))

cv2.imshow("test_image_regained", frame)


while True:
    k = cv2.waitKey(10)
    # print k
    if k == 27:
        break
