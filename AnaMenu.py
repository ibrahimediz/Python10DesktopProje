import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QListWidgetItem
from PyQt5 import uic
from DB.SozlukDB import SozlukDB
from OtelMenu import OtelMenu
import os


class AnaMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = SozlukDB()
        self.initUI()
    
    def initUI(self):
        self.win = uic.loadUi(os.getcwd()+os.sep+"\GUI\AnaMenu.ui")
        self.win.otelBilgi.triggered.connect(self.ac)
        self.win.show()
    
    def ac(self):
        self.otel = OtelMenu()
   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = AnaMenu()
    sys.exit(app.exec_())