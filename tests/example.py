import os
import sys
os.environ['QT_API'] = 'pyqt5'

import qtpy

from qtpy.QtWidgets import QApplication, QMainWindow
from qtpy.QtCore import QCoreApplication
from qtpylet import L, MapWidget

class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()
       
        self.mapWidget = MapWidget()
        self.setCentralWidget(self.mapWidget)
        self.map = L.map(self.mapWidget)
        self.map.setView([12.97, 77.59], 10)
        L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(self.map)
        self.show()
        
    def closeEvent(self, e=None):
        js = 'map.remove();'
        self.map.runJavaScript(js)
        print("close application")
app = QApplication(sys.argv)
app.exec_()