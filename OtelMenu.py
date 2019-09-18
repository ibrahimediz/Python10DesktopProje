import sys
from PyQt5.QtWidgets import QWidget,QApplication,QListWidgetItem,QMessageBox
from PyQt5 import uic
from DB.OtelMenuDB import OtelMenuDB
import os


class OtelMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.db = OtelMenuDB()
        self.initUI()
    
    def initUI(self):
        self.otel = uic.loadUi(os.getcwd()+os.sep+"\GUI\Otel.ui")
        self.otel.cmbIL.currentIndexChanged.connect(self.ilceDoldur)
        self.otel.btKaydet.clicked.connect(self.kaydetme)
        self.sozlukDoldur()
        self.ilDoldur()
        self.listeDoldur()
        self.otel.show()

    def sozlukDoldur(self):
        self.otel.cmbSinif.addItem("Seçiniz","-1")
        for ID,NUM in self.db.sozlukListe("3"):
            self.otel.cmbSinif.addItem(str(NUM),str(ID))
    def ilDoldur(self):
        self.otel.cmbIL.addItem("Seçiniz","-1")
        for ID,NUM in self.db.ilListe():
            self.otel.cmbIL.addItem(str(NUM),str(ID))
    def ilceDoldur(self,ilID):
        self.otel.cmbILCE.clear()
        self.otel.cmbILCE.addItem("Seçiniz","-1")
        for ID,NUM in self.db.ilceListe(self.otel.cmbIL.itemData(ilID)):
            self.otel.cmbILCE.addItem(str(NUM),str(ID)) 

    def duzenle(self,param):
        return "'" + param + "'"

    def kaydetme(self):
        OTEL_ADI= self.duzenle(self.otel.txtAdi.text())
        OTEL_IL= self.otel.cmbIL.itemData(self.otel.cmbIL.currentIndex())
        OTEL_ILCE= self.otel.cmbILCE.itemData(self.otel.cmbILCE.currentIndex())
        OTEL_TEL= self.duzenle(self.otel.txtTel.text())
        OTEL_ADRES= self.duzenle(self.otel.txtAdres.text())
        OTEL_TIP= self.otel.cmbSinif.itemData(self.otel.cmbSinif.currentIndex())
        OTEL_YILDIZ= self.otel.txtYildiz.text()
        if self.db.otelEkle(OTEL_ADI,OTEL_IL,OTEL_ILCE,OTEL_TEL,OTEL_ADRES,OTEL_TIP,OTEL_YILDIZ):
            QMessageBox.information("Bilgi","Kayıt Başarılı",QMessageBox.Ok,QMessageBox.Ok)

    def listeDoldur(self):
        liste =  self.db.OtelListe()
        for ID,Adi in liste:
            item = QListWidgetItem(str(ID)+"-"+Adi)
            self.otel.otelListe.addItem(item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = OtelMenu()
    sys.exit(app.exec_())