from DB.DB import DBTool
import os

class SozlukDB():
    def __init__(self):
        self.db = DBTool(os.getcwd()+os.sep+r"DB\OTELOTOMO.db")
    
    def sozlukListele(self,param = "1"):
        liste = self.db.select(TABLO="ST_SOZLUK",SUTUN=["ALAN_ID","ALAN_ADI"],SART="TABLO_ID = "+param)
        return liste

