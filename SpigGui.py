# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SpidGui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SpidGui(object):
    def setupUi(self, SpidGui):
        SpidGui.setObjectName("SpidGui")
        SpidGui.resize(400, 300)
        SpidGui.setFrameShape(QtWidgets.QFrame.StyledPanel)
        SpidGui.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label = QtWidgets.QLabel(SpidGui)
        self.label.setGeometry(QtCore.QRect(70, 30, 62, 16))
        self.label.setObjectName("label")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(SpidGui)
        self.doubleSpinBox.setGeometry(QtCore.QRect(190, 30, 69, 24))
        self.doubleSpinBox.setDecimals(0)
        self.doubleSpinBox.setMaximum(360.0)
        self.doubleSpinBox.setProperty("value", 320.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.buttonBox = QtWidgets.QDialogButtonBox(SpidGui)
        self.buttonBox.setGeometry(QtCore.QRect(100, 130, 164, 32))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.btUpdate = QtWidgets.QPushButton(SpidGui)
        self.btUpdate.setGeometry(QtCore.QRect(120, 80, 114, 32))
        self.btUpdate.setObjectName("btUpdate")

        self.retranslateUi(SpidGui)
        QtCore.QMetaObject.connectSlotsByName(SpidGui)

    def retranslateUi(self, SpidGui):
        _translate = QtCore.QCoreApplication.translate
        SpidGui.setWindowTitle(_translate("SpidGui", "Frame"))
        self.label.setText(_translate("SpidGui", "Heading"))
        self.btUpdate.setText(_translate("SpidGui", "Update"))

