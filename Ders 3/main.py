# Ödev

# Kullanıcıdan aldığınız sayının faktöriyelini hesaplayan ve sayının 10dan küçük olduğunu söyleyen program

# Notlar :Önce algoritmayı kurun sonra kodu yazın.
#      *Algoritma*
# 1 - Kullanıcıdan input alıyoruz
# 2 - İnput 10 dan küçükmü kontrolü
# 3 - Faktöriyel


"""
num = int(input("Faktöriyelin hesaplanmasını istediğiniz sayıyı yazınız : "))

factorial = 1
if num < 10:
# İşlemler
# Örn 5 faktöriyel 5x4x3x2x1 = 120
    for i in range(1,num+1):
        factorial *= i
    print(factorial)
else:
    print("Girilen sayı 10'dan büyük")

"""
"""
# While ile olan versiyonu
num = int(input("Faktöriyelin hesaplanmasını istediğiniz sayıyı yazınız : "))
factorial = 1
if num < 10:
    while num > 1:
        factorial *= num
        num -= 1
    print("Faktöriyel : " + str(factorial))
else :
    print("Lütfen 10'dan küçük bir sayı giriniz ! ")

"""
"""
# Fonksiyonlar
# Dğer dillerde :fun,func,function,procedure
def merhaba_dunya():
    print("Merhaba Dünya")

merhaba_dunya()

def carpim(sayi1,sayi2):
    sonuc = sayi1 * sayi2
    return sonuc

def toplama(sayi1,sayi2):
    return sayi1+sayi2

def bolme(sayi1,sayi2):
    return sayi1/sayi2
def cikarma(sayi1,sayi2):
    return sayi1-sayi2


carpimsonucu = carpim(3.8,4)
print("Carpim : " + str(carpimsonucu))

toplamasonucu = toplama(3,4)
print("Toplama : " + str(toplamasonucu))

bolmesonucu = bolme(20,3)
print("Bolme sonucu : " + str((bolmesonucu)))

cikarmasonucu = cikarma(4,3)
print("Cikarma islemi : " + str(cikarmasonucu))

"""
"""
# Faktöriyel işlemini fonksiyonla çağırma

def calcFactorial(num):
    factorial = 1
    if num < 10:
        for i in range(1, num + 1):
            factorial *= i

        return factorial
    else:
        print("Girilen sayı 10'dan büyük")
        return -1

kullanicidangelensayi = int(input("Lütfen Faktörüyelinin hesaplanmasını istediğiniz sayıyıyı yazınız : "))
faktoriyel = calcFactorial(kullanicidangelensayi)
print(faktoriyel)
if faktoriyel != -1:
    print("Faktöriyel : " + str(faktoriyel))
else:
    print("Lütfen 10 ve 1 arasında bir sayı giriniz ! ")

"""
"""
# Varsayılan Parametreler

def varsayilan(a,b = 0):
    print("a değeri : " + str(a))
    print("b değeri : " + str(b))

varsayilan(4,3)

def toplama(a,b = 0):
    return a + b

print("Toplama işlemi : " + str(toplama(5)))
"""
# Esnek sayida parametre
"""
# Normal parametre alan
def carpma(sayi1,sayi2 = 0):
    return sayi1*sayi2

print(str(carpma(20,5)))


def carpma(*sayilar):
    carpim = 1
    for sayi in sayilar:
        carpim *= sayi
    return carpim

sonuc = carpma(1,2,3,4)
print(str(sonuc))

"""
#kwargs
"""
dict = {"good":"iyi","bad":"kötü"}
print(dict["good"])
"""
"""
def sozluk(**kwargs):
    for anahtar,deger in kwargs.items():
        print("Anahtar : " + str(anahtar) + " Deger : " + str(deger))

sozluk(good = "iyi",bad="kotu")

"""
"""
# Lambda fonksiyonlar

kare=lambda x:x**2

def kare(x):
    return x**2

# print(str(kare(5)))

# Lambda ile hesap makinesi

toplam = lambda x,y:x+y
cikarma = lambda  x,y:x-y
bolme = lambda x,y:x/y
carpma = lambda x,y:x*y

print("Toplama işlemi : " + str(toplam(4,5)))
print("Cikarma işlemi : " + str(cikarma(4,5)))
print("Bolme işlemi : " + str(bolme(20,5)))
print("Carpma işlemi : " + str(carpma(4,5)))
"""
# Recursive(Özyinelemeli fonksiyonlar)
# Sürekli kendini çağıran fonksiyonlar
"""
def factorial(sayi):
    if sayi == 0:
        return 1
    else:
        return sayi * factorial(sayi-1) 

faktoriyelsonuc = factorial(6)
print(faktoriyelsonuc)
"""
def fibonacci(sayi):
    if sayi == 0:
        return 0
    elif sayi == 1:
        return  1
    else:
        return fibonacci(sayi-1) + fibonacci(sayi-2)

fibonaccisonuc = fibonacci(10)
print(str(fibonaccisonuc))