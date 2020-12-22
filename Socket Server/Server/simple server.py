#!/usr/bin/python           # This is server.py file



def camera_data():
    import cv2
    import numpy

    camera_port = 0
    ramp_frames = 15

    camera = cv2.VideoCapture(camera_port)

    def get_image():
       retval, im = camera.read()
       return im

    for i in xrange(ramp_frames):
     temp = get_image()

    print("Taking image...")
    camera_capture = get_image()

    frame = camera_capture

    frame = frame.flatten()
    data = frame.tostring()

    return data



def video_data():
    import cv2
    import numpy

    camera_port = 0
    ramp_frames = 15

    camera = cv2.VideoCapture(camera_port)

    def get_image():
       retval, im = camera.read()
       return im

    frame = get_image()

    frame = frame.flatten()
    data = frame.tostring()

    return data



import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

print host

s.listen(5)                 # Now wait for client connection.
while True:
    print 'hi'
    c, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr

    data = camera_data()

    c.send(data)
    c.close()                # Close the connection






