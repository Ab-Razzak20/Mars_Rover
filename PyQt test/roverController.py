# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rover_controller.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1233, 818)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.M1 = QtGui.QSlider(self.centralwidget)
        self.M1.setGeometry(QtCore.QRect(110, 100, 71, 22))
        self.M1.setOrientation(QtCore.Qt.Horizontal)
        self.M1.setObjectName(_fromUtf8("M1"))
        self.M2 = QtGui.QSlider(self.centralwidget)
        self.M2.setGeometry(QtCore.QRect(110, 150, 71, 22))
        self.M2.setOrientation(QtCore.Qt.Horizontal)
        self.M2.setObjectName(_fromUtf8("M2"))
        self.M3 = QtGui.QSlider(self.centralwidget)
        self.M3.setGeometry(QtCore.QRect(110, 200, 71, 22))
        self.M3.setOrientation(QtCore.Qt.Horizontal)
        self.M3.setObjectName(_fromUtf8("M3"))
        self.M4 = QtGui.QSlider(self.centralwidget)
        self.M4.setGeometry(QtCore.QRect(220, 100, 71, 22))
        self.M4.setOrientation(QtCore.Qt.Horizontal)
        self.M4.setObjectName(_fromUtf8("M4"))
        self.M5 = QtGui.QSlider(self.centralwidget)
        self.M5.setGeometry(QtCore.QRect(220, 150, 71, 22))
        self.M5.setOrientation(QtCore.Qt.Horizontal)
        self.M5.setObjectName(_fromUtf8("M5"))
        self.M6 = QtGui.QSlider(self.centralwidget)
        self.M6.setGeometry(QtCore.QRect(220, 200, 71, 22))
        self.M6.setOrientation(QtCore.Qt.Horizontal)
        self.M6.setObjectName(_fromUtf8("M6"))
        self.pushButton_m1f = QtGui.QPushButton(self.centralwidget)
        self.pushButton_m1f.setGeometry(QtCore.QRect(10, 90, 21, 41))
        self.pushButton_m1f.setObjectName(_fromUtf8("pushButton_m1f"))
        self.pushButton_m1h = QtGui.QPushButton(self.centralwidget)
        self.pushButton_m1h.setGeometry(QtCore.QRect(40, 90, 21, 41))
        self.pushButton_m1h.setObjectName(_fromUtf8("pushButton_m1h"))
        self.pushButton_m1n = QtGui.QPushButton(self.centralwidget)
        self.pushButton_m1n.setGeometry(QtCore.QRect(70, 90, 21, 41))
        self.pushButton_m1n.setObjectName(_fromUtf8("pushButton_m1n"))
        self.pushButton_m2f = QtGui.QPushButton(self.centralwidget)
        self.pushButton_m2f.setGeometry(QtCore.QRect(10, 140, 21, 41))
        self.pushButton_m2f.setObjectName(_fromUtf8("pushButton_m2f"))
        self.pushButton_m2h = QtGui.QPushButton(self.centralwidget)
        self.pushButton_m2h.setGeometry(QtCore.QRect(40, 140, 21, 41))
        self.pushButton_m2h.setObjectName(_fromUtf8("pushButton_m2h"))
        self.pushButton_m2n = QtGui.QPushButton(self.centralwidget)
        self.pushButton_m2n.setGeometry(QtCore.QRect(70, 140, 21, 41))
        self.pushButton_m2n.setObjectName(_fromUtf8("pushButton_m2n"))
        self.pushButton_m3f = QtGui.QPushButton(self.centralwidget)
        self.pushButton_m3f.setGeometry(QtCore.QRect(10, 190, 21, 41))
        self.pushButton_m3f.setObjectName(_fromUtf8("pushButton_m3f"))
        self.pushButton_m3h = QtGui.QPushButton(self.centralwidget)
        self.pushButton_m3h.setGeometry(QtCore.QRect(40, 190, 21, 41))
        self.pushButton_m3h.setObjectName(_fromUtf8("pushButton_m3h"))
        self.pushButton_m3n = QtGui.QPushButton(self.centralwidget)
        self.pushButton_m3n.setGeometry(QtCore.QRect(70, 190, 21, 41))
        self.pushButton_m3n.setObjectName(_fromUtf8("pushButton_m3n"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 161, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.MotorPower = QtGui.QSlider(self.centralwidget)
        self.MotorPower.setGeometry(QtCore.QRect(30, 41, 231, 31))
        self.MotorPower.setOrientation(QtCore.Qt.Horizontal)
        self.MotorPower.setObjectName(_fromUtf8("MotorPower"))
        self.checkBox_motor = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_motor.setGeometry(QtCore.QRect(190, 70, 111, 20))
        self.checkBox_motor.setMinimumSize(QtCore.QSize(111, 20))
        self.checkBox_motor.setMaximumSize(QtCore.QSize(111, 16777215))
        self.checkBox_motor.setObjectName(_fromUtf8("checkBox_motor"))
        self.roverAngle_X = QtGui.QGraphicsView(self.centralwidget)
        self.roverAngle_X.setGeometry(QtCore.QRect(20, 250, 131, 131))
        self.roverAngle_X.setObjectName(_fromUtf8("roverAngle_X"))
        self.roverAngle_Y = QtGui.QGraphicsView(self.centralwidget)
        self.roverAngle_Y.setGeometry(QtCore.QRect(170, 250, 131, 131))
        self.roverAngle_Y.setObjectName(_fromUtf8("roverAngle_Y"))


        self.scene = QtGui.QGraphicsScene()
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setScene(self.scene)

        # self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(330, 60, 881, 621))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))

        self.graphicsView_2 = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(20, 450, 291, 231))
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1233, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_m1f.setText(_translate("MainWindow", "F", None))
        self.pushButton_m1h.setText(_translate("MainWindow", "H", None))
        self.pushButton_m1n.setText(_translate("MainWindow", "N", None))
        self.pushButton_m2f.setText(_translate("MainWindow", "F", None))
        self.pushButton_m2h.setText(_translate("MainWindow", "H", None))
        self.pushButton_m2n.setText(_translate("MainWindow", "N", None))
        self.pushButton_m3f.setText(_translate("MainWindow", "F", None))
        self.pushButton_m3h.setText(_translate("MainWindow", "H", None))
        self.pushButton_m3n.setText(_translate("MainWindow", "N", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Motors Power Control:</span></p></body></html>", None))
        self.checkBox_motor.setText(_translate("MainWindow", "Same as Left", None))

