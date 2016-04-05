from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class GeoLocationWidget(QtWidgets.QWidget):

  __pyqtSignals__ = ("latitudeChanged(double)",
                     "longitudeChanged(double)")

  def __init__(self, parent = None):

     QtWidgets.QWidget.__init__(self, parent)


     latitudeLabel = QLabel(self.tr("Latitude:"))
     self.latitudeSpinBox = QDoubleSpinBox()
     self.latitudeSpinBox.setRange(-90.0, 90.0)
     self.latitudeSpinBox.setDecimals(5)

     longitudeLabel = QLabel(self.tr("Longitude:"))
     self.longitudeSpinBox = QDoubleSpinBox()
     self.longitudeSpinBox.setRange(-180.0, 180.0)
     self.longitudeSpinBox.setDecimals(5)

     #self.connect(self.latitudeSpinBox,
     #    SIGNAL("valueChanged(double)"),
     #    self, SIGNAL("latitudeChanged(double)"))
     #self.connect(self.longitudeSpinBox,
     #    SIGNAL("valueChanged(double)"),
     #    self, SIGNAL("longitudeChanged(double)"))

     layout = QGridLayout(self)
     layout.addWidget(latitudeLabel, 0, 0)
     layout.addWidget(self.latitudeSpinBox, 0, 1)
     layout.addWidget(longitudeLabel, 1, 0)
     layout.addWidget(self.longitudeSpinBox, 1, 1)
