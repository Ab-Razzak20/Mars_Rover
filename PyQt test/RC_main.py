import sys
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PIL import Image
from PIL import ImageQt

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

        print 'should displayed'


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())


