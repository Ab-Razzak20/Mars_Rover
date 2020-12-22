import socket
import pygame
from PIL import Image, ImageTk
import sys
from StringIO import StringIO
import time


#Create a var for storing an IP address:
#ip = raw_input("Please enter the IP address: ")
# ip = socket.gethostname()
#ip = 'raspberrypi'

ip = '192.168.0.103'

#Start PyGame:
pygame.init()
#Create a PyGame screen, and set its size to 640x480L
screen = pygame.display.set_mode((960,720))
#Set the window caption:
pygame.display.set_caption('Remote Webcam Viewer')
#Load a font:
font = pygame.font.SysFont("Arial",14)
#Create a PyGame clock which will be used to limit the fps:
clock = pygame.time.Clock()

#Create some more var's:
timer = 0
previousImage = ""
image = ""


import thread
count = 0

# def thread_t():
#     global count
#     while 1:
#         time.sleep(5)
#         print "FPS = " + str((count/5))
#         count = 0
#
# thread.start_new_thread(thread_t, ())


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip,5000))

#Main program loop:
while 1:

    #Check if the exit button has been pressed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #We use a timer to limit how many images we request from the server each second:
    if timer < 1:

        rdata = ""

        while(1):
            # connect was previously here

            data = client_socket.recv(28672)
            rdata = rdata + data[1:]
            # print len(rdata)
            if data[0] == '0':
                break



        data = rdata
        # print len(data)

        timer = 0

    else:

        #Count down the timer:
        timer -= 1

    #We store the previous recieved image incase the client fails to recive all of the data for the new image:
    previousImage = image

    #We use a try clause to the program will not abort if there is an error:
    try:

        zObj = StringIO()
        zObj.write(data)

        im = Image.open(zObj)
        new_str = im.tobytes()

        mode = im.mode
        size = im.size
        data = im.tobytes()

        image = pygame.image.fromstring(data, size, mode)

    except:
        #If we failed to recieve a new image we display the last image we revieved:
        image = previousImage
        print "showing last image"

    #Set the var output to our image:
    output = image

    output = pygame.transform.scale(output, (960, 720))

    #We use PyGame to blit the output image to the screen:
    screen.blit(output,(0,0))

    #We set our clock to tick 60 times a second, which limits the frame rate to that amount:
    clock.tick(60)
    #We update the screen:
    pygame.display.flip()


    count = count + 1




