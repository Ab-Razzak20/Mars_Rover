import socket
import pygame
import sys
from StringIO import StringIO
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PIL import Image, ImageTk, ImageQt
from PyQt4 import QtCore, QtGui
from roverController import Ui_MainWindow

from PIL import Image


im = Image.open('a.jpg')
image = ImageQt.ImageQt(im)



class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.ui.checkBox_motor.stateChanged.connect(self.checBoxMotor)
        self.ui.pushButton_m1f.clicked.connect(self.button_m1f)
        self.ui.M1.valueChanged.connect(self.M1)


    def button_m1f(self):
        print 'pressed'
        self.ui.checkBox_motor.click()
        print self.ui.checkBox_motor.checkState()
        print self.ui.M1.value()
        self.ui.M1.setValue(50)
        img = Image.open('a.jpg')
        self.display_image(img)


    def checBoxMotor(self, state):
        a=1
        # print state
        # print QtCore.Qt.Checked
        # print "check box"

    def M1(self, vlu):
        print "slide"
        print vlu


    def display_image(self, img):
        self.ui.scene.clear()
        w, h = img.size
        self.imgQ = ImageQt.ImageQt(img)  # we need to hold reference to imgQ, or it will crash
        pixMap = QPixmap.fromImage(self.imgQ)
        self.ui.scene.addPixmap(pixMap)
        self.ui.graphicsView.fitInView(QRectF(0, 0, w, h), Qt.KeepAspectRatio)
        self.ui.scene.update()



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
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()

    myapp.main()

    sys.exit(app.exec_())


