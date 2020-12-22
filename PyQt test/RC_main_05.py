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

ip = socket.gethostname()
# ip = 'raspberrypi'
# ip = '192.168.0.103'

q = Queue.Queue()

im = Image.open('map_a_building.png')
nn = Image.open('None.jpg')
rover_X0 = Image.open('rover_X.png')
rover_Y0 = Image.open('rover_Y.png')

# X_angle = 10
# Y_angle = -20

image = ImageQt.ImageQt(im)

image_Map = im
PWM_speed = 255

time1 = 0
time2 = 0

# count = 0
# def thread_t():
#     global count
#     while 1:
#         time.sleep(5)
#         print "FPS = " + str((count/5))
#         count = 0
#
# thread.start_new_thread(thread_t, ())


class MyForm(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.ui.checkBox_motor.stateChanged.connect(self.checBoxMotor)
        self.ui.pushButton_m1f.clicked.connect(self.button_m1f)
        self.ui.MotorPower.valueChanged.connect(self.MotorPower)

        self.ui.lcd.display(PWM_speed)

        self.ui.textBrowser.setFontPointSize(11)
        self.ui.textBrowser.append("Temperature: 27 C")
        self.ui.textBrowser.update()




    def closeEvent(self, event):
        print "Bye Bye :)"
        sys.exit()

    def keyPressEvent(self, event):
        key = event.key()
        # print(key)
        # print QtCore.Qt.Key_A
        if key == QtCore.Qt.Key_Left:
            print('Left Arrow Pressed')
        elif key == QtCore.Qt.Key_Escape:
            self.close()

        elif key == QtCore.Qt.Key_W:
            self.send_cmd('1'+str(PWM_speed))
        elif key == QtCore.Qt.Key_D:
            self.send_cmd('2'+str(PWM_speed))
        elif key == QtCore.Qt.Key_S:
            self.send_cmd('3'+str(PWM_speed))
        elif key == QtCore.Qt.Key_A:
            self.send_cmd('4'+str(PWM_speed))


        elif key == QtCore.Qt.Key_0:
            self.send_cmd('s')
        elif key == QtCore.Qt.Key_1:
            self.send_cmd('1')
        elif key == QtCore.Qt.Key_2:
            self.send_cmd('2')
        elif key == QtCore.Qt.Key_3:
            self.send_cmd('3')



        # event.accept()

    def keyReleaseEvent(self, event):
        key = event.key()
        # print key



    def send_cmd(self, data):
        global time1, time2
        print "dflaaaaaaafssdd"

        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((ip, 5005))
            client_socket.sendall(data)
            time.sleep(.2)

        except:
            print "Error in sending cmd (port 5005)"




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

    def MotorPower(self, vlu):
        global PWM_speed
        PWM_speed = 255 * vlu / 99
        self.ui.lcd.display(PWM_speed)


    # def display_image(self, img):
    #     self.ui.scene.clear()
    #     w, h = img.size
    #     self.imgQ = ImageQt.ImageQt(img)  # we need to hold reference to imgQ, or it will crash
    #     pixMap = QPixmap.fromImage(self.imgQ)
    #     self.ui.scene.addPixmap(pixMap)
    #     self.ui.graphicsView.fitInView(QRectF(0, 0, w, h), Qt.KeepAspectRatio)
    #     self.ui.scene.update()
    #
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             sys.exit()



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

            X_angle = int(img)

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

            Y_angle = - int(img)

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




    def main(self):

        # global Y_angle



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

                    try:
                        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        client_socket.connect((ip,5000))
                        data = client_socket.recv(28672)
                    except:
                        print "Error in thread 1 (port 5000)"
                        time.sleep(1)
                        continue

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

                # time.sleep(2)





        # def thread2():
        #
        #     print "thread-2 started"
        #
        #     image = ""
        #
        #     # Main program loop:
        #     while 1:
        #         # We use a timer to limit how many images we request from the server each second:
        #
        #         rdata = ""
        #
        #         while (1):
        #             client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #             client_socket.connect((ip, 5001))
        #
        #             data = client_socket.recv(28672)
        #             rdata = rdata + data[1:]
        #             # print len(rdata)
        #             if data[0] == '0':
        #                 break
        #
        #         data = rdata
        #         # print len(data)
        #
        #         # We store the previous recieved image incase the client fails to recive all of the data for the new image:
        #         self.previousImage = image
        #
        #         # We use a try clause to the program will not abort if there is an error:
        #         try:
        #
        #             zObj = StringIO()
        #             zObj.write(data)
        #
        #             im = Image.open(zObj)
        #
        #             image = im
        #
        #
        #
        #         except:
        #             # If we failed to recieve a new image we display the last image we revieved:
        #             image = self.previousImage
        #             print "showing last image"
        #
        #
        #         if self.ui.radioButton_5.isChecked() == True:
        #             i2 = image_Map
        #         else:
        #             i2 = image
        #
        #         # Y_angle = Y_angle + 1
        #
        #         if (q.qsize() > 5):
        #             q.queue.clear()
        #         q.put(('2', i2))


        def thread_stable():
            while 1:
                q.put(('2', image_Map))
                time.sleep(.05)


        def thread_data():

            # global X_angle, Y_angle

            while 1:
                try:
                    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client_socket.connect((ip, 5003))
                    data = client_socket.recv(1000)
                except:
                    print "Error in thread_data (port 5003)"
                    time.sleep(1)
                    continue


                x = ""
                y = ""

                i = 0
                while i < len(data):

                    if(data[i] == 'R'):
                        for j in range (1, 8):
                            x = x + data[i+j]
                            if(data[i+j+1] == ':'):
                                i = i + j + 1
                                break

                    if(data[i] == 'P'):
                        for j in range(1, 8):
                            y = y + data[i + j]
                            if (data[i + j + 1] == ':'):
                                i = i + j + 1
                                break

                    i = i + 1



                q.put(('X', y))
                q.put(('Y', x))

                time.sleep(.1)




        thread.start_new_thread(thread1, ())
        # thread.start_new_thread(thread2, ())
        thread.start_new_thread(thread_stable, ())
        # thread.start_new_thread(thread_data, ())




        self.display_image_partial('X', '0')
        self.display_image_partial('Y', '0')

        t1 = 0

        while 1:
            iit, img = q.get()
            try:
                # if iit=='1':
                #     t2 = time.time()
                #     print (t2 - t1) * 1000
                #     t1 = time.time()

                self.display_image_partial(iit, img)
            except:
                print "error in PyQt"




if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()

    myapp.main()
    app.exec_()
    sys.exit()






