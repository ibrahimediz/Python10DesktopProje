import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QListWidgetItem,QComboBox
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot,pyqtSignal
from DB.AnaMenuDB import AnaMenuDB
from OtelMenu import OtelMenu
import os


class AnaMenu(QMainWindow):
    gunSay = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.db = AnaMenuDB()
        self.initUI()
    
    def initUI(self):
        self.otelSecim = ""
        self.win = uic.loadUi(os.getcwd()+os.sep+"\GUI\AnaMenu.ui")
        self.win.otelBilgi.triggered.connect(self.ac)
        self.win.txtGun.textChanged.connect(self.gunGonder)
        self.MusteriDoldur()
        self.OdaDoldur()
        self.win.show()


    def gunGonder(self):
        gunsay = self.win.txtGun.text()
        self.gunSay.emit(gunsay)
    
    def ac(self):
        self.otel = OtelMenu(self)
        self.otel.tetikleme(self)
        
        

    def MusteriDoldur(self):
        self.win.cmbMusteri.addItem("Seçiniz","-1")
        for item in self.db.MusteriListe():
            self.win.cmbMusteri.addItem(str(item[1]+" "+item[2]),str(item[0]))
    
    def OdaDoldur(self):
        if self.otelSecim:
            self.win.cmbOda.addItem("Seçiniz","-1")
            for ID,NUM in self.db.OdaListe(self.otelSecim):
                self.win.cmbOda.addItem(str(NUM),str(ID))

    def secilen(self,index):
        combo = self.sender()
        print(combo.itemData(index))

    def otelSecildi(self,val=0):
        self.win.cmbOda.clear()
        liste = self.db.OdaListe(val)
        if liste:
            self.win.cmbOda.addItem("Seçiniz","-1")
        for ID,NUM in liste:
            self.win.cmbOda.addItem(str(NUM),str(ID))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = AnaMenu()
    sys.exit(app.exec_())