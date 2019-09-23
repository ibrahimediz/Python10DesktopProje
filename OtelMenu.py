import sys
from PyQt5.QtWidgets import QWidget,QApplication,QListWidgetItem,QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot,pyqtSignal
from DB.OtelMenuDB import OtelMenuDB
import os


class OtelMenu(QWidget):
    def __init__(self,parent):
        super(OtelMenu,self).__init__(parent)
        self.db = OtelMenuDB()
        self.initUI()
        self.parent = parent
    
    def initUI(self):
        self.otel = uic.loadUi(os.getcwd()+os.sep+"GUI\Otel.ui")
        self.otel.cmbIL.currentIndexChanged.connect(self.ilceDoldur)
        self.otel.btKaydet.clicked.connect(self.kaydetme)
        self.otel.otelListe.doubleClicked.connect(self.secim)
        self.otel.btTemizle.clicked.connect(self.doldur)
        self.otel.btOtelSec.clicked.connect(self.otelSecim)
        self.sozlukDoldur()
        self.ilDoldur()
        self.listeDoldur()
        self.otel.show()

    def otelSecim(self):
        self.parent.otelSecildi(self.otel.lblOtelID.text())
        self.otel.close()

    def secim(self):
        secilen = self.otel.otelListe.currentItem().text()
        ID =  secilen.split('-')[0]
        secilenBilgi =  self.db.OtelListe(ID)[0]
        self.doldur(secilenBilgi)

    def doldur(self,secilenBilgi=[]):
        if secilenBilgi:
            self.otel.lblOtelID.setText(str(secilenBilgi[0]))
            self.otel.txtAdi.setText(secilenBilgi[1])
            self.otel.cmbIL.setCurrentIndex(secilenBilgi[2])
            self.comboSecimYap(secilenBilgi[3],self.otel.cmbILCE)
            self.comboSecimYap(secilenBilgi[6],self.otel.cmbSinif)
            self.otel.txtYildiz.setText(str(secilenBilgi[7]))
            self.otel.txtTel.setText(str(secilenBilgi[4]))
            self.otel.txtAdres.setText(str(secilenBilgi[5]))
        else:
            self.otel.lblOtelID.setText("")
            self.otel.txtAdi.setText("")
            self.otel.cmbIL.setCurrentIndex(0)
            self.otel.cmbILCE.clear()
            self.otel.cmbSinif.setCurrentIndex(0)
            self.otel.txtYildiz.setText("")
            self.otel.txtTel.setText("")
            self.otel.txtAdres.setText("")

    def gunsayYaz(self,val=0):
        self.otel.lblGun.setText(val)

    def tetikleme(self,anamenu=None):
        anamenu.gunSay.connect(self.gunsayYaz)


    def comboSecimYap(self,itemData = 0,combo=None):
        for i in range(combo.count()):
            if combo.itemData(i) == str(itemData):
                combo.setCurrentIndex(i)


    def sozlukDoldur(self):
        self.otel.cmbSinif.addItem("Seçiniz","-1")
        for ID,NUM in self.db.sozlukListe("3"):
            self.otel.cmbSinif.addItem(str(NUM),str(ID))
    def ilDoldur(self):
        self.otel.cmbIL.addItem("Seçiniz","-1")
        for ID,NUM in self.db.ilListe():
            self.otel.cmbIL.addItem(str(NUM),str(ID))
    def ilceDoldur(self,ilID):
        if ilID != -1:
            self.otel.cmbILCE.clear()
            self.otel.cmbILCE.addItem("Seçiniz","-1")
            for ID,NUM in self.db.ilceListe(self.otel.cmbIL.itemData(ilID)):
                self.otel.cmbILCE.addItem(str(NUM),str(ID)) 

    def duzenle(self,param):
        return "'" + param + "'"

    def kaydetme(self):
        sonuc = None
        if self.otel.lblOtelID.text() == "":
            OTEL_ADI= self.duzenle(self.otel.txtAdi.text())
            OTEL_IL= self.otel.cmbIL.itemData(self.otel.cmbIL.currentIndex())
            OTEL_ILCE= self.otel.cmbILCE.itemData(self.otel.cmbILCE.currentIndex())
            OTEL_TEL= self.duzenle(self.otel.txtTel.text())
            OTEL_ADRES= self.duzenle(self.otel.txtAdres.text())
            OTEL_TIP= self.otel.cmbSinif.itemData(self.otel.cmbSinif.currentIndex())
            OTEL_YILDIZ= self.otel.txtYildiz.text()
            sonuc = self.db.otelEkle(OTEL_ADI,OTEL_IL,OTEL_ILCE,OTEL_TEL,OTEL_ADRES,OTEL_TIP,OTEL_YILDIZ)
        else:
            OTEL_ID = self.otel.lblOtelID.text()
            OTEL_ADI= self.duzenle(self.otel.txtAdi.text())
            OTEL_IL= self.otel.cmbIL.itemData(self.otel.cmbIL.currentIndex())
            OTEL_ILCE= self.otel.cmbILCE.itemData(self.otel.cmbILCE.currentIndex())
            OTEL_TEL= self.duzenle(self.otel.txtTel.text())
            OTEL_ADRES= self.duzenle(self.otel.txtAdres.text())
            OTEL_TIP= self.otel.cmbSinif.itemData(self.otel.cmbSinif.currentIndex())
            OTEL_YILDIZ= self.otel.txtYildiz.text()
            elCevap =  QMessageBox.question(self,"Soru","Kaydetmek İstediğine Emin misin?",QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,QMessageBox.Cancel)
            if elCevap == QMessageBox.Yes:
                sonuc = self.db.otelGuncelle(OTEL_ID,OTEL_ADI,OTEL_IL,OTEL_ILCE,OTEL_TEL,OTEL_ADRES,OTEL_TIP,OTEL_YILDIZ)
            elif elCevap == QMessageBox.No:
                self.doldur()
        if sonuc:
            QMessageBox.information(self,"Bilgi","Kayıt Başarılı",QMessageBox.Ok,QMessageBox.Ok)
            self.listeDoldur()
        else:
            QMessageBox.warning(self,"Bilgi","Kayıt Başarısız",QMessageBox.Ok,QMessageBox.Ok)

    def listeDoldur(self):
        self.otel.otelListe.clear()
        liste =  self.db.OtelListe()
        for ID,Adi in liste:
            item = QListWidgetItem(str(ID)+"-"+Adi)
            self.otel.otelListe.addItem(item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = OtelMenu(app)
    sys.exit(app.exec_())