import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import uic
import os


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.win = uic.loadUi(os.getcwd()+os.sep+"ilkUI.ui")
        self.win.btilk.clicked.connect(self.tiklandi)
        self.win.show()
       
    def tiklandi(self):
        self.win.lblDurum.setText("Merhaba "+self.win.txtAdi.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())