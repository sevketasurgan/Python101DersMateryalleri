class Araba:
    marka = ""
    model = ""
    yil = 0
    yas = ""
    def __init__(self,marka,model,yil):
        self.marka = marka
        self.model = model
        self.yil = yil
        print("Marka " + self.marka + " Model " + self.model)

    def aracYasHesapla(self):
        print("Aracın yası : " + str(2023-int(self.yil)))