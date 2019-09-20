from DB.DB import DBTool
import os


class OtelMenuDB():
    def __init__(self):
        self.db = DBTool(os.getcwd()+os.sep+"DB\OTELOTOMO.db")



    def OtelListe(self,sart =""):
        if sart:
            return self.db.select(TABLO="OTEL_BILGI",
            SUTUN=["*"],SART = "OTEL_ID = "+sart)
        else:    
            return self.db.select(TABLO="OTEL_BILGI",SUTUN=["OTEL_ID","OTEL_ADI"])

    def ilListe(self):
        return self.db.select(TABLO="ST_ILLER",SUTUN=["IL_ID","IL_ADI"])
    def ilceListe(self,il_id):
        return self.db.select(TABLO="ST_ILCELER",SUTUN=["ST_ILCE_ID","ST_ILCE_ADI"],SART="ST_IL = "+il_id)

    def sozlukListe(self,tabloID):
        return self.db.select(TABLO="ST_SOZLUK",SUTUN=["ALAN_ID","ALAN_ADI"],SART="TABLO_ID = "+tabloID)
    
    def otelEkle(self, OTEL_ADI,
                           OTEL_IL,
                           OTEL_ILCE,
                           OTEL_TEL,
                           OTEL_ADRES,
                           OTEL_TIP,
                           OTEL_YILDIZ):
        return self.db.insert(TABLO="OTEL_BILGI",SUTUN=[                           "OTEL_ADI",
                           "OTEL_IL",
                           "OTEL_ILCE",
                           "OTEL_TEL",
                           "OTEL_ADRES",
                           "OTEL_TIP",
                           "OTEL_YILDIZ"],DEGER=
                           [OTEL_ADI,
                           OTEL_IL,
                           OTEL_ILCE,
                           OTEL_TEL,
                           OTEL_ADRES,
                           OTEL_TIP,
                           OTEL_YILDIZ])


    def otelGuncelle(self, OTEL_ID,OTEL_ADI,
                           OTEL_IL,
                           OTEL_ILCE,
                           OTEL_TEL,
                           OTEL_ADRES,
                           OTEL_TIP,
                           OTEL_YILDIZ):
        return self.db.update(TABLO="OTEL_BILGI",SUTUN=[                           "OTEL_ADI",
                           "OTEL_IL",
                           "OTEL_ILCE",
                           "OTEL_TEL",
                           "OTEL_ADRES",
                           "OTEL_TIP",
                           "OTEL_YILDIZ"],DEGER=
                           [OTEL_ADI,
                           OTEL_IL,
                           OTEL_ILCE,
                           OTEL_TEL,
                           OTEL_ADRES,
                           OTEL_TIP,
                           OTEL_YILDIZ],SART = "OTEL_ID = "+OTEL_ID)