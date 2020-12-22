import socket
import pygame
import sys
from StringIO import StringIO
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PIL import Image, ImageTk, ImageQt
from PyQt4 import QtCore, QtGui
from roverController_02 import Ui_MainWindow
import time
from PIL import Image, ImageDraw, ImageFont


im = Image.open('map_a_building1.png')
nn = Image.open('None.jpg')
rover_X0 = Image.open('rover_X.png')
rover_Y0 = Image.open('rover_Y.png')

X_angle = 7
Y_angle = -3

image = ImageQt.ImageQt(im)

image_Map = im


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.ui.checkBox_motor.stateChanged.connect(self.checBoxMotor)
        self.ui.pushButton_m1f.clicked.connect(self.button_m1f)
        self.ui.M1.valueChanged.connect(self.M1)

        self.ui.textBrowser.setFontPointSize(11)
        self.ui.textBrowser.append("Temperature: 27 C")
        self.ui.textBrowser.update()


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


    def display_image_02(self, img, img2):
        global rover_X0, rover_Y0, X_angle, Y_angle

        self.ui.scene.clear()
        self.ui.scene2.clear()
        self.ui.sceneX.clear()
        self.ui.sceneY.clear()


        img2 = img2.resize((400,300))
        rover_X = rover_X0.rotate(X_angle)
        rover_Y = rover_Y0.rotate(Y_angle)

        drawX = ImageDraw.Draw(rover_X)
        # # drawX.line((0,235, 470,235), fill=228)
        # # drawX.line((235,0 ,235, 470), fill=228)
        font = ImageFont.truetype("arial.ttf", 62)
        drawX.text((90, 330),"Angle: " + str(X_angle),(0,0,255),font=font)
        #
        drawY = ImageDraw.Draw(rover_Y)
        # # drawX.line((0,235, 470,235), fill=228)
        # # drawX.line((235,0 ,235, 470), fill=228)
        font2 = ImageFont.truetype("arial.ttf", 75)
        drawY.text((90, 380),"Angle: " + str(Y_angle),(0,0,255),font=font2)


        w, h = img.size
        w2, h2 = img2.size

        wX, hX = rover_X.size
        wY, hY = rover_Y.size

        self.imgQ = ImageQt.ImageQt(img)  # we need to hold reference to imgQ, or it will crash
        self.imgQ2 = ImageQt.ImageQt(img2)
        self.imgQX = ImageQt.ImageQt(rover_X)
        self.imgQY = ImageQt.ImageQt(rover_Y)


        pixMap = QPixmap.fromImage(self.imgQ)
        pixMap2 = QPixmap.fromImage(self.imgQ2)
        pixMapX = QPixmap.fromImage(self.imgQX)
        pixMapY = QPixmap.fromImage(self.imgQY)

        self.ui.scene.addPixmap(pixMap)
        self.ui.scene2.addPixmap(pixMap2)
        self.ui.sceneX.addPixmap(pixMapX)
        self.ui.sceneY.addPixmap(pixMapY)

        self.ui.graphicsView.fitInView(QRectF(0, 0, w, h), Qt.KeepAspectRatio)
        self.ui.graphicsView_2.fitInView(QRectF(0, 0, w2, h2), Qt.KeepAspectRatio)
        self.ui.graphicsView_X.fitInView(QRectF(0, 0, wX, hX), Qt.KeepAspectRatio)
        self.ui.graphicsView_Y.fitInView(QRectF(0, 0, wY, hY), Qt.KeepAspectRatio)

        self.ui.scene.update()
        self.ui.scene2.update()
        self.ui.sceneX.update()
        self.ui.sceneY.update()


    def main(self):

        global X_angle, Y_angle

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

            self.display_image_02(im, nn)



            time.sleep(.5)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()

    myapp.main()

    sys.exit(app.exec_())


