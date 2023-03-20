# Python Ders 2
"""
x = 25
y = 25
z = 10

if x<10:
    print("x, 10'dan küçüktür")
elif x!=y:
    print("x,y ye eşit değildir.")
else:
    print("Koşullar çalışmadı.")

if x>z:print("x,z'den büyüktür.") # Short hand -ternary tek satır if bloğu

# & == and
# elif -> else if
if x!=y and x>z:
    print("x, y ye eşit değil ve x büyüktür y den")

# or operatöründe ikisinden birisi doğru
if x==y or x>y:
    print("x ' ye ye eşit veya x büyüktür y den")

# not operatörü koşulu tersine çevirir.
print(x>y)
if not x>y:
    print("x ' y den büyük ")

# Nested If Bağıntılı koşul
if x==y:
    if x>z:
        print("x y ye eşit vs x z den büyük")
else:
    print("Koşullar tutmadı.")

# If kullanımında boş bırakılamaz - pass anahtar kelimesi kullanılır
a = 55
b = 155

if a > b:
    pass
"""
"""
# Not ortalaması hesaplayan ve geçip geçmediğini gösteren program

vize = float(input("Vizenizi giriniz: "))
final = float(input("Finalinizi girin: "))
sonuc = (vize * 0.4) + (final *0.6)
gecmenotu = 60

if (sonuc >= gecmenotu) and sonuc <= 100:
    print("Dersten gectiniz. Notunuz : " + str(sonuc))
elif (sonuc < gecmenotu) and sonuc <= 100:
    print("Dersten Kaldınız! Notunuz : " + str(sonuc))
else:
    print("Hatalı değer girdiniz.")
"""

"""
# Girilen sayının çift veya tek olduğunu söyleyen program

number = int(input("Sayıyı giriniz : "))

if number % 2 == 0:
    print("Sayı çifttir.")
elif number % 2 == 1:
    print("Sayı tektir")
    
"""

# Girilen sayıların toplamı 100 den büyükmü diye kontrol eden program

"""
num1 = int(input("Birinci sayıyı giriniz:"))
num2 = int(input("İkinci sayıyı giriniz"))

toplam = num1 + num2

if toplam > 100:
    print("Sayıların toplamı 100 den büyüktür. Toplam : " + str(toplam))
elif toplam <100:
    print("Sayıların toplamı 100 den küçüktür Toplam : " + str(toplam))
elif toplam == 100:
    print("Sayıların toplamı 100 e eşit Toplam : " + str(toplam))
else:
    print("İstenmeyen değer")
"""
"""
# Girilen kelimede ilk harf e harfimi

kelime = input("Lütfen bir kelime giriniz : ")
arananharf = input("Aradığınız harf : ")

if kelime[0] == arananharf:
    print("Girilen kelime "+arananharf+" harfiyle başlıyor")
elif kelime[0] != arananharf:
    print("Girilen kelime "+arananharf+" harfi ile başlamıyor.")
else:
    print("İstenmeyen değer")
"""
"""
# Döngüler - While Döngüsü

x = 0
while x<5:
    print(x)
    x+=1

"""
"""
# Kullanıcıdan sayı girişi alarak toplamını hesaplayan program
total = 0
while True:
    num = int(input("Bir sayı girin : (Çıkmak için 0 ' a basın)"))
    if num == 0:
        break
    total += num
print("Toplam Sayı -> " + str(total))

"""


# Liste içerisindeki elemanları yazdırma - Iterasyon
liste = ["elma","armut","çilek","kiraz"]
index = 0

while index < len(liste) :
    print(liste[index])
    index += 1


# Döngüler - For Döngüsü - Iterasyon (Iteration)
"""
meyveler = ["karpuz","elma","ananas","muz"]

for meyve in meyveler:
    print(meyve)
    
"""
"""
meyveler = ["karpuz","elma","ananas","muz"]

# range komutu
for i in range(0,4):
    print(meyveler[i])
"""

"""
kelime = "python"

for harf in kelime:
    print(harf)
    
"""

"""
# Dizi içerisindeki sayıların toplamını hesaplayan program
sayilar = [1,2,3,5,6,11]
total = 0
for sayi in sayilar:
    total += sayi
print("Toplam = " + str(total))
"""
"""
# Liste içerisindeki çift sayıları yazdıran program
sayilar = [2,4,5,7,3,87,92,246]

for sayi in sayilar:
    if sayi % 2 == 0:
        print(sayi)



"""

# Ödev

# Kullanıcıdan aldığınız sayının faktöriyelini hesaplayan ve sayının 10dan küçük olduğunu söyleyen program

# Notlar :Önce algoritmayı kurun sonra kodu yazın.
#      *Algoritma*
# 1 - Kullanıcıdan input alıyoruz
# 2 - İnput 10 dan küçükmü kontrolü
# 3 - Faktöriyel










