import socket
import pygame.camera
import pygame.image


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(),5000))
server_socket.listen(5)


print "Your IP address is: ", socket.gethostbyname(socket.gethostname())


pygame.camera.init()
cameras = pygame.camera.list_cameras()

print "Using camera %s ..." % cameras[0]

webcam = pygame.camera.Camera(cameras[0])
webcam.start()

# grab first frame
sf = pygame.Surface((640,480))
image = webcam.get_image(sf)


print "Server Waiting for client on port 5000"

while 1:

    client_socket, address = server_socket.accept()

    sf = pygame.Surface((640,480))
    image = webcam.get_image(sf)
    # ---- convert to RGB if not

    #image = image.resize((120,90))

    #image.save("webcam.jpg")
    image = pygame.transform.scale(image, (96, 72))

    data = pygame.image.tostring(image, "RGB")

    client_socket.sendall(data)

