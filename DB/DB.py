import sqlite3 as sql

class DBTool():
    def __init__(self,adres):
        self.adres =adres

    def connectDB(self):
        self.db = sql.connect(self.adres)
        self.cur = self.db.cursor()

    def select(self,**kwargs):
        try:
            self.connectDB()
            sutun = ""
            sart = " 1=1 "
            for key,value in kwargs.items():
                if key == "TABLO":
                    tablo = value
                elif key == "SUTUN":
                    if value[0] == "*":
                        sutun = value[0]
                    else:
                        for item in value:
                            sutun += item + ","
                        else:
                            sutun = sutun.rstrip(",")
                elif key == "SART":
                    sart = value
            sorgu = "SELECT {} FROM {} WHERE {}".format(sutun,tablo,sart)
            self.cur.execute(sorgu)
            liste = self.cur.fetchall()
        except Exception as hata:
            liste = [hata]
        finally:
            self.db.close()
            return liste
    

    def insert(self,**kwargs):
        sonuc = None
        try:
            self.connectDB()
            sutun = ""
            deger= ""
            for key,value in kwargs.items():
                if key == "TABLO":
                    tablo = value
                elif key == "SUTUN":
                    for item in value:
                        sutun += item + ","
                    else:
                        sutun = sutun.rstrip(",")
                elif key == "DEGER":
                    for item in value:
                        deger += item + ","
                    else:
                        deger = deger.rstrip(",")
            sorgu = """
            INSERT INTO {} ({}) VALUES ({}) """.format(tablo,sutun,deger)
            self.cur.execute(sorgu)
            self.db.commit()
            sonuc = True
        except Exception as hata:
            print(hata)
            sonuc = False
        finally:
            self.db.close()
            return sonuc

    def update(self,**kwargs):
        sonuc = None
        sutun = []
        deger = []
        guncel = ""
        sart = " 1=1 "
        try:
            self.connectDB()
            for key,value in kwargs.items():
                if key == "TABLO":
                    tablo = value
                elif key == "SUTUN":
                    sutun = value
                elif key == "DEGER":
                    deger = value
                elif key == "SART":
                    sart = value
            for i in range(0,len(sutun)):
                guncel += "{} = {},".format(sutun[i],deger[i])
            guncel = guncel.rstrip(",")
            sorgu = """
            UPDATE {} SET {} WHERE {} """.format(tablo,guncel,sart)
            self.cur.execute(sorgu)
            self.db.commit()
            sonuc = True
        except Exception as hata:
            print(hata)
            sonuc = False
        finally:
            self.db.close()
            return sonuc

    def delete(self,**kwargs):
        sonuc = None
        sart = ""
        tablo = ""
        try:
            self.connectDB()
            tablo = kwargs["TABLO"]
            sart =  kwargs["SART"]
            sorgu = """ DELETE FROM {} WHERE {}""".format(tablo,sart)
            self.cur.execute(sorgu)
            self.db.commit()
            sonuc = True
        except Exception as hata:
            print(hata)
            sonuc = False
        finally:
            self.db.close()
            return sonuc

             
        




            


