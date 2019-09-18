import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QListWidgetItem,QComboBox
from PyQt5 import uic
from DB.AnaMenuDB import AnaMenuDB
from OtelMenu import OtelMenu
import os


class AnaMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = AnaMenuDB()
        self.initUI()
    
    def initUI(self):
        self.win = uic.loadUi(os.getcwd()+os.sep+"\GUI\AnaMenu.ui")
        self.win.otelBilgi.triggered.connect(self.ac)
        self.win.cmbMusteri.currentIndexChanged.connect(self.secilen)
        self.win.cmbOda.currentIndexChanged.connect(self.secilen)
        self.MusteriDoldur()
        self.OdaDoldur()
        self.win.show()
    
    def ac(self):
        self.otel = OtelMenu()
    
    def MusteriDoldur(self):
        self.win.cmbMusteri.addItem("Seçiniz","-1")
        for item in self.db.MusteriListe():
            self.win.cmbMusteri.addItem(str(item[1]+" "+item[2]),str(item[0]))
    
    def OdaDoldur(self):
        self.win.cmbOda.addItem("Seçiniz","-1")
        for ID,NUM in self.db.OdaListe():
            self.win.cmbOda.addItem(str(NUM),str(ID))

    def secilen(self,index):
        combo = self.sender()
        print(combo.itemData(index))

    # def secilenMus(self,index):
    #     print(self.secilenDataAl(self.win.cmbMusteri,index))

    # def secilenOda(self,index):
    #     print(self.secilenDataAl(self.win.cmbMusteri,index))  

    # def secilenDataAl(self,combo,index):
    #     return combo.itemData(index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = AnaMenu()
    sys.exit(app.exec_())