import socket, thread, time, threading
import pygame
import sys
from StringIO import StringIO
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PIL import Image, ImageTk, ImageQt
from PyQt4 import QtCore, QtGui
from roverController_02 import Ui_MainWindow

from PIL import Image, ImageDraw, ImageFont
import Queue

q = Queue.Queue()

im = Image.open('map_a_building.png')
nn = Image.open('None.jpg')
rover_X0 = Image.open('rover_X.png')
rover_Y0 = Image.open('rover_Y.png')

X_angle = 10
Y_angle = -20

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

    def keyPressEvent(self, event):
        key = event.key()
        print(key)
        # print QtCore.Qt.Key_A
        if key == QtCore.Qt.Key_Left:
            print('Left Arrow Pressed')
        elif key == QtCore.Qt.Key_Escape:
            self.close()
        # event.accept()

    def keyReleaseEvent(self, event):
        key = event.key()
        # print key




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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()



    def display_image_partial(self, N, img):
        global rover_X0, rover_Y0, X_angle, Y_angle

        if(N == '1'):
            self.ui.scene.clear()
            w, h = img.size
            self.imgQ = ImageQt.ImageQt(img)  # we need to hold reference to imgQ, or it will crash
            pixMap = QPixmap.fromImage(self.imgQ)
            self.ui.scene.addPixmap(pixMap)
            self.ui.graphicsView.fitInView(QRectF(0, 0, w, h), Qt.KeepAspectRatio)
            self.ui.scene.update()

        elif(N == '2'):
            self.ui.scene2.clear()
            img = img.resize((400, 300))
            w, h = img.size
            self.imgQ2 = ImageQt.ImageQt(img)  # we need to hold reference to imgQ, or it will crash
            pixMap2 = QPixmap.fromImage(self.imgQ2)
            self.ui.scene2.addPixmap(pixMap2)
            self.ui.graphicsView_2.fitInView(QRectF(0, 0, w, h), Qt.KeepAspectRatio)
            self.ui.scene2.update()

        elif(N == 'X'):

            self.ui.sceneX.clear()
            rover_X = rover_X0.rotate(X_angle)

            drawX = ImageDraw.Draw(rover_X)
            # drawX.line((0,235, 470,235), fill=228)
            # drawX.line((235,0 ,235, 470), fill=228)
            font = ImageFont.truetype("arial.ttf", 62)
            drawX.text((90, 330), "Angle: " + str(X_angle), (0, 0, 255), font=font)

            wX, hX = rover_X.size

            self.imgQX = ImageQt.ImageQt(rover_X)
            pixMapX = QPixmap.fromImage(self.imgQX)
            self.ui.sceneX.addPixmap(pixMapX)
            self.ui.graphicsView_X.fitInView(QRectF(0, 0, wX, hX), Qt.KeepAspectRatio)
            self.ui.sceneX.update()


        elif (N == 'Y'):

            self.ui.sceneY.clear()
            rover_Y = rover_Y0.rotate(Y_angle)

            drawY = ImageDraw.Draw(rover_Y)
            # drawX.line((0,235, 470,235), fill=228)
            # drawX.line((235,0 ,235, 470), fill=228)
            font2 = ImageFont.truetype("arial.ttf", 75)
            drawY.text((90, 380), "Angle: " + str(Y_angle), (0, 0, 255), font=font2)

            wY, hY = rover_Y.size

            self.imgQY = ImageQt.ImageQt(rover_Y)
            pixMapY = QPixmap.fromImage(self.imgQY)
            self.ui.sceneY.addPixmap(pixMapY)
            self.ui.graphicsView_Y.fitInView(QRectF(0, 0, wY, hY), Qt.KeepAspectRatio)
            self.ui.sceneY.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()




    def display_image_all(self, img, img2):
        global rover_X0, rover_Y0, X_angle, Y_angle

        self.ui.scene.clear()
        self.ui.scene2.clear()
        self.ui.sceneX.clear()
        self.ui.sceneY.clear()

        # img = img.resize((640,480))
        img2 = img2.resize((400,300))
        rover_X = rover_X0.rotate(X_angle)
        rover_Y = rover_Y0.rotate(Y_angle)

        drawX = ImageDraw.Draw(rover_X)
        # drawX.line((0,235, 470,235), fill=228)
        # drawX.line((235,0 ,235, 470), fill=228)
        font = ImageFont.truetype("arial.ttf", 62)
        drawX.text((90, 330),"Angle: " + str(X_angle),(0,0,255),font=font)

        drawY = ImageDraw.Draw(rover_Y)
        # drawX.line((0,235, 470,235), fill=228)
        # drawX.line((235,0 ,235, 470), fill=228)
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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


    def main(self):

        global Y_angle

        ip = socket.gethostname()
        #ip = 'raspberrypi'

        #Start PyGame:
        pygame.init()
        # screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('Remote Webcam Viewer')


        #Create some more var's:


        def thread1():

            print "thread started"

            image = ""


            #Main program loop:
            while 1:

                #We use a timer to limit how many images we request from the server each second:


                rdata = ""

                while(1):
                    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client_socket.connect((ip,5000))

                    data = client_socket.recv(32768)
                    rdata = rdata + data[1:]
                    # print len(rdata)
                    if data[0] == '0':
                        break


                data = rdata
                # print len(data)

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


                if self.ui.radioButton.isChecked() == True:
                    i1 = image_Map
                else:
                    i1 = image


                # Y_angle = Y_angle + 1

                if(q.qsize() > 5):
                    q.queue.clear()

                q.put(('1', i1))




        def thread2():

            print "thread-2 started"

            image = ""

            # Main program loop:
            while 1:

                # We use a timer to limit how many images we request from the server each second:

                rdata = ""

                while (1):
                    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client_socket.connect((ip, 5001))

                    data = client_socket.recv(32768)
                    rdata = rdata + data[1:]
                    # print len(rdata)
                    if data[0] == '0':
                        break

                data = rdata
                # print len(data)

                # We store the previous recieved image incase the client fails to recive all of the data for the new image:
                self.previousImage = image

                # We use a try clause to the program will not abort if there is an error:
                try:

                    zObj = StringIO()
                    zObj.write(data)

                    im = Image.open(zObj)

                    image = im



                except:
                    # If we failed to recieve a new image we display the last image we revieved:
                    image = self.previousImage
                    print "showing last image"


                if self.ui.radioButton_5.isChecked() == True:
                    i2 = image_Map
                else:
                    i2 = image

                # Y_angle = Y_angle + 1

                if (q.qsize() > 5):
                    q.queue.clear()
                q.put(('2', i2))



        thread.start_new_thread(thread1, ())
        thread.start_new_thread(thread2, ())

        # T1 = threading.Thread(target=thread1)
        # T2 = threading.Thread(target=thread2)
        # T1.start()
        # T2.start()


        self.display_image_partial('X', "")
        self.display_image_partial('Y', "")

        ii = 0
        while 1:
            iit, img = q.get()
            self.display_image_partial(iit, img)
            ii = ii+1





if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()

    myapp.main()

    sys.exit(app.exec_())

