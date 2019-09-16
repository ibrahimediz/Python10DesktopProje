import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QListWidgetItem
from PyQt5 import uic
from DB.SozlukDB import SozlukDB
import os


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = SozlukDB()
        self.initUI()
    
    def initUI(self):
        self.win = uic.loadUi(os.getcwd()+os.sep+"ilkUI.ui")
        self.win.btilk.clicked.connect(self.tiklandi)
        self.win.cmbOdaTip.currentIndexChanged.connect(self.tiklandi)
        self.win.liste.doubleClicked.connect(self.listeSecim)
        self.comboDoldur()
        self.listeDoldur()
        self.win.show()
    
    def listeDoldur(self):
        liste = self.db.sozlukListele(param="1 OR 1=1")
        for item in liste:
            yazi = str(item[0]) + "-" + item[1]
            nesne =  QListWidgetItem(yazi)
            self.win.liste.addItem(nesne)

    def listeSecim(self):
        print(self.win.liste.currentItem().text())
        secilen = int(self.win.liste.currentItem().text().split("-")[0])
        yazi = self.win.liste.currentItem().text().split("-")[1]
        self.win.txtAdi.setText(yazi)
        self.win.cmbOdaTip.setCurrentIndex(secilen)

    def comboDoldur(self):
        liste = self.db.sozlukListele("1")
        self.win.cmbOdaTip.addItem("Seçiniz","-1")
        for ID,adi in liste:
            self.win.cmbOdaTip.addItem(str(adi),str(ID))
        liste = self.db.sozlukListele("2")
        for ID,adi in liste:
            self.win.cmbCinsiyet.addItem(str(adi),str(ID))

    def tiklandi(self):
        secilen = self.win.cmbOdaTip.currentIndex()
        self.win.lblDurum.setText(str(secilen) +" Seçildi")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())