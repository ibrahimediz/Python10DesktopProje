import sys
from PyQt5.QtWidgets import QWidget,QApplication,QListWidgetItem
from PyQt5 import uic
from DB.SozlukDB import SozlukDB
import os


class OtelMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.db = SozlukDB()
        self.initUI()
    
    def initUI(self):
        self.win = uic.loadUi(os.getcwd()+os.sep+"\GUI\Otel.ui")
        self.win.pushButton.clicked.connect(self.close)
        self.win.show()

   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = OtelMenu()
    sys.exit(app.exec_())