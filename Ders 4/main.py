class Kedi:
    isim = ""
    #Constructor(Yapıcı) tanımlama

    def miyavla(self):
        print("miyav")

# Kalıtım (Inheritance)
class EvKedisi(Kedi):
    def uyku(self):
        print("Kedi uyuyor")

kedinesnesi = Kedi() # Instance

evkedisinesnesi = EvKedisi()
evkedisinesnesi.miyavla()

evkedisinesnesi.uyku()


class Araba:
    marka = ""
    model = ""
    yili = ""
    fiyat = ""
    km = ""
    renk = ""
    beygir = ""
    #Constructor
    def __init__(self,marka,model,yili,fiyat,km,renk,beygir):
        self.marka = marka
        self.model = model # self -> this
        self.yili = yili
        self.fiyat = fiyat
        self.km = km
        self.renk = renk
        self.beygir = beygir


BirinciAraba = Araba("Togg","T10X","2023","100000","0","mavi","200")
print(BirinciAraba.marka + " " + BirinciAraba.model + " " + BirinciAraba.yili + " " + BirinciAraba.fiyat + " " + BirinciAraba.km + " " + BirinciAraba.renk + " " + BirinciAraba.beygir)

İkinciAraba = Araba("Ford","Focus","2023","100000","220","turuncu","300")
print(İkinciAraba.marka + " " + İkinciAraba.model + " " + İkinciAraba.yili + " " + İkinciAraba.fiyat + " " + İkinciAraba.km + " " + İkinciAraba.renk + " " + İkinciAraba.beygir)

"""
class ArabaFiyat(Araba):
    fiyat = Araba.fiyat
    def fiyatYazdir(self,fiyat):
        print("Arabanın Fiyatı : " + fiyat)


arabaFiyat = ArabaFiyat(BirinciAraba.marka,BirinciAraba.model,BirinciAraba.yili,BirinciAraba.fiyat,BirinciAraba.km,BirinciAraba.renk,BirinciAraba.beygir)
arabaFiyat.fiyatYazdir()

"""

class Ogrenci:
    isim = ""
    soyisim = ""
    yas = ""
    not_ort = ""
    numara = ""
    def __init__(self,isim,soyisim,yas,not_ort,numara):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
        self.not_ort = not_ort
        self.numara = numara
    def notYazdir(self,isim):
        if isim == self.isim:
            print(self.not_ort)


ogrenci1 = Ogrenci("Ahmet","Kaplan,", "12", "99", "12345")





# Polimorfizm (Çok biçimlilik )
print(len("Python"))
print(len([1 , 2 ,3]))







