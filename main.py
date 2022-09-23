import sqlite3
import time

class Sarki():
    def __init__(self,isim,sanatci,album,sirket,sure):
        self.isim = isim
        self.sanatci = sanatci
        self.album = album
        self.sirket = sirket
        self.sure = sure

    def __str__(self):
        return (f"Şarkı İsmi : {self.isim}\nSanatçı : {self.sanatci}\nAlbüm : {self.album}\nŞirket : {self.sirket}\nSüre : {self.sure}\n")


class Spotify():
    def __init__(self):

        self.baglanti_olustur()

    def baglanti_olustur(self):
        
        self.baglanti = sqlite3.connect("C:\\Users\\ahmet\\OneDrive\\Masaüstü\\yazilim\\KeepPy\\sarki_db\\sarkilar.db")
        self.cursor = self.baglanti.cursor()

        sorgu = "CREATE TABLE IF NOT EXISTS sarkilar (Şarkı İsmi TEXT,Sanatçı TEXT,Albüm TEXT,Şirket TEXT,Süre INT)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()

    def baglantiyi_kes(self):

        self.baglanti.close()

    def sarkilari_goster(self):

        sorgu = ("SELECT * FROM sarkilar")

        self.cursor.execute(sorgu)

        sarkilar = self.cursor.fetchall()

        if (len(sarkilar) == 0):
            print("Hiçbir şarkı bulunamadı")
        else:
            for i in sarkilar:
                
                sarki = Sarki(i[0],i[1],i[2],i[3],i[4])
                print(sarki)

    def sarki_sorgula(self,isim):

        sorgu = ("SELECT * FROM sarkilar WHERE Şarkı = ?")

        self.cursor.execute(sorgu,(isim,))

        sarkilar = self.cursor.fetchall()

        if (len(sarkilar)== 0):
            print("Böyle bir şarkı bulunamadı")
        else:

            sarki = Sarki(sarkilar[0][0],sarkilar[0][1],sarkilar[0][2],sarkilar[0][3],sarkilar[0][4])
            print(sarki)

    def sarki_ekle(self,sarki):
        
        sorgu = ("INSERT INTO sarkilar Values(?,?,?,?,?)")

        self.cursor.execute(sorgu,(sarki.isim,sarki.sanatci,sarki.album,sarki.sirket,sarki.sure))

        self.baglanti.commit()

    def sarki_sil(self,isim):

        sorgu = ("DELETE FROM sarkilar WHERE Şarkı = ?")

        self.cursor.execute(sorgu,(isim,))

        self.baglanti.commit()

    def toplam_sure(self):

        sorgu = ("SELECT Süre FROM sarkilar")

        self.cursor.execute(sorgu)

        sureler = self.cursor.fetchall()

        toplam = 0

        for i in sureler:
            toplam += i[0]

        print(f"Toplam şarkıların süresi : {toplam} Saniyedir")


print("""*****************************

Spotify Programına Hoşgeldiniz.

İşlemler : 

1.Şarkıları Göster
2.Şarkı Sorgulama
3.Şarkı Ekleme
4.Şarkı Silme
5.Toplam Süreyi Göster

Çıkmak için "q" ya basınız.

*****************************

""")

spotify = Spotify()

while True:
    islem = input("Yapacağınız İşlem : ")

    if (islem == "q"):
        print("Program Sonlandırılıyor...")
        break
    elif (islem == "1"):
        spotify.sarkilari_goster()
    elif (islem == "2"):
        isim = input("Şarkı İsmi Giriniz : ")
        spotify.sarki_sorgula(isim)
    elif (islem == "3"):
        isim = input("Şarkı İsmi Giriniz : ")
        sanatci = input("Sanatçı İsmi Giriniz : ")
        album = input("Albüm İsmi Giriniz : ")
        sirket = input("Şirket İsmi Giriniz : ")
        sure = int(input("Süreyi Giriniz (saniye) : "))

        sarki = Sarki(isim,sanatci,album,sirket,sure)

        spotify.sarki_ekle(sarki)
        time.sleep(1)

        print("Şarkı Eklendi")

    elif (islem == "4"):
        isim = input("Şarkı İsmi Giriniz : ")

        spotify.sarki_sil(isim)
        time.sleep(1)
        print("Şarkı Silindi..")

    elif (islem == "5"):
        spotify.toplam_sure()