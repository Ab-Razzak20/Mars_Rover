import sys

from PyQt4 import QtCore, QtGui
from test_web import Ui_Dialog

class MyForm(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


    def helloworld(self):

        print "hello new"

        while 1:
            self.ui.QWebView.changeEvent(self, self.ui.QEvent)

        print ("Hello world again")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())


