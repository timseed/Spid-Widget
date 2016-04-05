
from PyQt5 import QtCore, QtGui, QtWidgets
from progress import Ui_Form
import time

class progress2 (Ui_Form):

     def __init__(self):
         super(progress2,self).__init__()
         self.timer = QtCore.QBasicTimer()
         print("I am born")
         self.setupUi()
        

     def setupUi(self):
        super(progress2,self).setupUi(self)
        print("I am setup")
        junk=1

     def timerEvent(self, event):
          print("timerEven Went off")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = progress2()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
