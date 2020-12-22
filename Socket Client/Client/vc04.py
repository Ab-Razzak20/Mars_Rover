import socket
import pygame
from PIL import Image, ImageTk, ImageQt
import sys
from StringIO import StringIO
from PyQt4.QtCore import *
from PyQt4.QtGui import *



class TestWidget(QWidget):
    def __init__(self, parent=None):

        self.im3 = ''
        self.previousImage = ""

        QWidget.__init__(self, parent)
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.button = QPushButton("Do test")

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.view)
        self.setLayout(layout)

        self.button.clicked.connect(self.do_test)


    def do_test(self):
        img = Image.open('img_temp.jpg')
        self.display_image(self.previousImage)


    def display_image(self, img):
        self.scene.clear()
        w, h = img.size
        self.imgQ = ImageQt.ImageQt(img)  # we need to hold reference to imgQ, or it will crash
        pixMap = QPixmap.fromImage(self.imgQ)
        self.scene.addPixmap(pixMap)
        self.view.fitInView(QRectF(0, 0, w, h), Qt.KeepAspectRatio)
        self.scene.update()



    def main(self):
        ip = socket.gethostname()
        #ip = 'raspberrypi'

        #Start PyGame:
        pygame.init()
        screen = pygame.display.set_mode((640,480))
        pygame.display.set_caption('Remote Webcam Viewer')


        #Create some more var's:
        timer = 0
        image = ""

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
                    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client_socket.connect((ip,5000))

                    data = client_socket.recv(20480)
                    rdata = rdata + data[1:]
                    print len(rdata)
                    if data[0] == '0':
                        break



                data = rdata
                print len(data)

                timer = 0

            else:

                #Count down the timer:
                timer -= 1

            #We store the previous recieved image incase the client fails to recive all of the data for the new image:
            self.previousImage = image

            #We use a try clause to the program will not abort if there is an error:
            try:

                zObj = StringIO()
                zObj.write(data)

                im = Image.open(zObj)

                image = im



            except:
                #If we failed to recieve a new image we display the last image we revieved:
                image = self.previousImage
                print "showing last image"

            self.display_image(image)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = TestWidget()
    widget.resize(640, 480)
    widget.show()

    widget.main()

    sys.exit(app.exec_())

