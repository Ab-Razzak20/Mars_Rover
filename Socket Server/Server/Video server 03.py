import socket
import pygame.camera
import pygame.image

from PIL import Image
from StringIO import StringIO
import time


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(),5000))
server_socket.listen(5)



print "Your IP address is: ", socket.gethostbyname(socket.gethostname())


pygame.camera.init()
cameras = pygame.camera.list_cameras()

print cameras

print "Using camera %s ..." % cameras[0]

webcam = pygame.camera.Camera(cameras[0])
webcam.start()

# grab first frame
sf = pygame.Surface((640,480))
image = webcam.get_image(sf)

E = 0

print "Server Waiting for client on port 5000"


def sendData(x1):
    try:
        client_socket.sendall(x1)
        return 0

    except:
        print "Error while sending.."
        return 404

client_socket, address = server_socket.accept()

while 1:

    sf = pygame.Surface((640,480))
    image = webcam.get_image(sf)

    # ---- convert to RGB if not


    # ---- resize image
    image = pygame.transform.scale(image, (640, 480))

    data = pygame.image.tostring(image, "RGB")

    # ---- now its time to reduce size (compress)
    img = Image.frombytes('RGB', (640, 480), data)
    zdata = StringIO()
    img.save(zdata, 'JPEG')

    new_data = zdata.getvalue()

    splitSize = 32768-1
    i = 0
    if(len(new_data) >= splitSize):
        while(1):
            x = new_data[i*splitSize : (i+1)*splitSize]
            i+=1

            if len(x) < splitSize:
                # print len(x)
                x = str(0) + x

                sendData(x)

                break


            x = str(1) + x

            rt = sendData(x)
            if rt == 404:
                break


    else:
        new_data = str(0) + new_data
        sendData(new_data)

