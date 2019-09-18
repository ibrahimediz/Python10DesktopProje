from DB.DB import DBTool
import os


class AnaMenuDB():
    def __init__(self):
        self.db = DBTool(os.getcwd()+os.sep+"DB\OTELOTOMO.db")



    def MusteriListe(self):
        return self.db.select(TABLO="MUS_BILGI",SUTUN=["*"])

    def OdaListe(self,param="1"):
        return self.db.select(TABLO="OTEL_ODA_BILGI",SUTUN=["ODA_ID","ODA_NUM"],SART="OTEL_ID="+param)
