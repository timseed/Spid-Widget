# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SpidGui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(392, 300)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout = QtWidgets.QVBoxLayout(Frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Direction = QtWidgets.QScrollBar(Frame)
        self.Direction.setOrientation(QtCore.Qt.Horizontal)
        self.Direction.setObjectName("Direction")
        self.verticalLayout.addWidget(self.Direction)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Frame)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.verticalLayout.addWidget(self.doubleSpinBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(Frame)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))

