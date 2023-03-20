
# Python 101 - Ders 1

# Numbers
x = 2 # Integer(tam sayılar)
y = 2.1 # Float(ondalıklı sayılar)
z = 2.3j # Complex(Karmaşık sayılar)


print(type(x))
print(type(y))
print(type(z))

# Strings

cumle = 'Ben python ogreniyorum.'
print(cumle)

cumle2 = "Ben python ogreniyorum."
print(cumle2)

cumle3 = """
    Bu bir paragraf
    Bu bir paragraf
    Bu bir paragraf
    
"""
print(cumle3)

print(type(cumle))
print(type(cumle2))
print(type(cumle3))

print(cumle[1]) # Diziler 0 dan başlar.
print(cumle[1:6])

print(cumle[4])

print(len(cumle)) # len length'in kısaltılmışı

birlestirmecumlesi = "Kodlama yapıyorum"
print(cumle + birlestirmecumlesi) # Concatenation - Birlestirme
print("-----Listeler-------")
# Listeler

liste1 = ["elma","karpuz","domates"]
print(type(liste1))
print(liste1[0])



liste2 = [1,2,5,3]
print(liste2[3])

liste3 = [1,11,30,"ahmet"]
print(liste3[3])

print(len(liste3))

liste3.append("mehmet") # Ekleme işlemi
print(liste3[4])

liste3.remove("mehmet") # çıkarma işlemi
# print(liste3[4])

liste2.sort()
print(liste2)

# Yorum İşareti Satır olarak
"""
 Çoklu satır yorumu
"""

liste4 = liste2 + liste3 # Liste birleştirme
print(liste4)

liste5 = ["samet","esra","gokce"]
print(liste5)
liste5[1] = "ayse"
print(liste5)

liste6 = ["samet","esra","gokce"]
print(liste6)
liste6[0:2] = ["osman","mahmut","ercan"]
print(liste6)


liste6.insert(2,"degistirdik")
print(liste6)

kopyaliste6 = liste6.copy() # liste kopyalama
print(kopyaliste6)

kopyaliste6.reverse() # ters
print(kopyaliste6)


# Demetler(Tuples)

demet1 = (1,2,5,3,2) # tuple demet
print(type(demet1))

print(len(demet1))

print(demet1[0])

# demet1[1] = 55
#print(demet1)

print(demet1.count(2)) # tekrarlanma sıklığı

# Dictionaries - Sözlük

sozluk1 = {"1234":"Osman","4532":"Mehmet",3:["Bir","İki", "Uc"]}
print(type(sozluk1))
print("Kullanıcı " + sozluk1["1234"])


print(len(sozluk1))

print(sozluk1[3])

# sozluk1.pop("1234")
# print(sozluk1)

sozlukkopya = sozluk1.copy()
print(sozlukkopya)

print(sozluk1.get("4532"))

print(sozluk1.keys()) # anahtarları elde etme

# CRUD Operations create  read update delete


# Boolean

x = True
y = False
a = 2

print(x)
print(y)

print(type(x))
print(a == 2)

# Operatörler
a = 5
b = 4
c = "9"

print(a + b) # Toplama
print(a - b) # Çıkarma
print(a*b) # Çarpma
print(a/b) # Bolme
print(20 % 2) # Mod alma

print(b**2) # Üs alma

a *= 5
#a = a * 5
print(a)

# Karşılaştırma

x = 10
y = 10

print(x == 10)
print(x == y)

print(x != 10) # x eşit değildir 10 sayısına
print(x != y) # x eşit değildir 10 sayısına

print(x < 10) # x küçüktür 10
print(x <= 10) # x küçük eşittir 10

print(x > 10) # x büyüktür 10
print(x >= 10) # x büyüktür eşittir 10

# Mantıksal Operatörler

print(x<10 and y< 10) # And  ve operatörü
print(x<10 or y<=10) # or - veya operatörü
print(not(x<10 or y<=10)) # Not operatörü

# Kimlik Operatörü

print(x is y) # is operatörü
print(x is not y) # is not operatörü

#Üyelik Operatörü
list_member = ["ahmet","mehmet"]

print("ahmet" not in list_member)

# Tip Dönüşümleri - Type Casting

#x = input() #girdi almak için kullanılıyor.
#print(int(x) % 2) # Type casting - tip dönüşümü Integer - tamsayı
#print(float(x) + 2) # Type casting - tip dönüşümü Float - ondalıklı sayı

sayi = 4 # integer - tamsayı
#print(int(sayi) / 2) # Type casting - tip dönüşümü

print("Sayımız -> " + str(sayi)) # Type casting - tip dönüşümü

list_1 = "Python"

print(type(list_1))
print(list_1)
list_new = list(list_1)
print(type(list_new))

list_to_tuple = tuple(list_new)
print(type(list_to_tuple))

















