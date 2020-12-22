import socket, thread, time, threading
import pygame
import sys
from StringIO import StringIO
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PIL import Image, ImageTk, ImageQt
from PyQt4 import QtCore, QtGui
from roverController_04 import Ui_MainWindow

from PIL import Image, ImageDraw, ImageFont
import Queue

# ip = socket.gethostname()
# ip = 'raspberrypi'
ip = '192.168.0.104'

q = Queue.Queue()

im = Image.open('map_a_building.png')
nn = Image.open('None.jpg')
rover_X0 = Image.open('rover_X.png')
rover_Y0 = Image.open('rover_Y.png')

# X_angle = 10
# Y_angle = -20

image = ImageQt.ImageQt(im)

image_Map = im
PWM_speed = 0

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

        self.ui.checkBox_motor.setChecked(True)
        self.ui.checkBox_motor1.setChecked(True)
        self.ui.checkBox_motor2.setChecked(True)
        self.ui.checkBox_motor3.setChecked(True)



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

        elif key == QtCore.Qt.Key_U:
            self.send_cmd('51')
        elif key == QtCore.Qt.Key_J:
            self.send_cmd('52')
        elif key == QtCore.Qt.Key_I:
            self.send_cmd('53')
        elif key == QtCore.Qt.Key_K:
            self.send_cmd('54')
        elif key == QtCore.Qt.Key_O:
            self.send_cmd('55')
        elif key == QtCore.Qt.Key_L:
            self.send_cmd('56')

        elif key == QtCore.Qt.Key_N:
            self.send_cmd('57')
        elif key == QtCore.Qt.Key_M:
            self.send_cmd('58')



        # elif key == QtCore.Qt.Key_0:
        #     self.send_cmd('s')
        # elif key == QtCore.Qt.Key_1:
        #     self.send_cmd('1')
        # elif key == QtCore.Qt.Key_2:
        #     self.send_cmd('2')
        # elif key == QtCore.Qt.Key_3:
        #     self.send_cmd('3')



        # event.accept()

        time.sleep(.1)



    def keyReleaseEvent(self, event):

        if event.isAutoRepeat():
            # print "auto"
            return

        key = event.key()
        # print key
        if key == QtCore.Qt.Key_W or key == QtCore.Qt.Key_D or key == QtCore.Qt.Key_S or key == QtCore.Qt.Key_A or key == QtCore.Qt.Key_U or key == QtCore.Qt.Key_J or key == QtCore.Qt.Key_I or key == QtCore.Qt.Key_K or key == QtCore.Qt.Key_O or key == QtCore.Qt.Key_L:
            self.send_cmd('00')
            # print "released"



    def send_cmd(self, data):
        global time1, time2

        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((ip, 5005))
            client_socket.sendall(data)


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



        def thread_stable():

            current_cam = 0
            new_cam = 0

            current_mottors_powered = 111
            new_mottors_powered = 111
            mp1 = 1
            mp2 = 1
            mp3 = 1

            while 1:
                q.put(('2', image_Map))
                time.sleep(.05)

                if self.ui.radioButton_5.isChecked() == True:
                    new_cam = 9

                elif self.ui.radioButton_6.isChecked() == True:
                    new_cam = 0

                elif self.ui.radioButton_7.isChecked() == True:
                    new_cam = 1

                elif self.ui.radioButton_8.isChecked() == True:
                    new_cam = 2

                if new_cam != current_cam:
                    self.send_cmd('9' + str(new_cam))
                    current_cam = new_cam
                    print "camera changed to " + str(new_cam)



                mp1 = self.ui.checkBox_motor1.isChecked()
                mp2 = self.ui.checkBox_motor2.isChecked()
                mp3 = self.ui.checkBox_motor3.isChecked()

                new_mottors_powered = mp1*100 + mp2*10 + mp3

                if new_mottors_powered != current_mottors_powered:
                    self.send_cmd('8' + str(new_mottors_powered))
                    current_mottors_powered = new_mottors_powered
                    print "Motor power combination changed to " + str(new_mottors_powered)


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






