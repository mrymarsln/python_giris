# list()
# değiştirilebilir,farklı tipte verileri bir arada tutabilir,sıralı(index işlemleri yapabilir)
notlar=[90,80,70,60]
print(type(notlar))

liste=['a',19.3,90]
list_genis=['a',19.3,90,notlar]
print(list_genis)
print(len(list_genis))

print(list_genis[0])
print(list_genis[1])
print(list_genis[3])

print(type(list_genis[3]))

tum_liste=[liste,list_genis]
print(tum_liste)

# LİSTE METODLARI
# eleman ekleme,silme ve değiştirme 
liste=['ali','veli','berkcan','ayse']
print(liste)

liste[1]='velinin_babasi' # 1. indexe 'velinin_babası' yazdırır
print(liste)

liste[0:3]='alinin_babasi','velinin_babasi','berkcanın_babasi' # 0 dan 3. indexe kadar atadığımız değerleri yazdırır
print(liste)

liste=['ali','veli','berkcan','ayse'] 
liste=liste+['kemal'] # listeye 'kemal' değişkenini ekler
print(liste)

del liste[2] # listenin içindeki 2. indexi siler
print(liste)

# liste metodları
liste2=['ali','veli','isik']

liste2.append('ahmet') # listeye eleman ekleme
print(liste2)

liste2.remove('isik') # listeden eleman silme
print(liste2)

# .pop & .insert
# insert => vermiş olduğumuz indexe göre elemen ekler
liste3=['ali','veli','ahmet']
liste3.insert(0,'ayse') # 0. indexe ayse karakterini yazdırır
print(liste3)
 
liste3.insert(len(liste3),'beren')  # listenin sonuna beren karakterini yazdırır
print(liste3)

# pop => vermiş olduğumuz indexe göre elemean siler
liste3=['ali','veli','ahmet']
liste3.pop(2)
print(liste3)

# count => hangi karakterden kaç tane olduğunu gösterir
liste4=['ali','veli','isik','ali','veli']
print(liste4)

# copy => yedekleme yapmak istediğimizde kullanırız
liste_yedek=liste4.copy()
print(liste_yedek)

# extend => iki listeyi birleştirmek istediğimizde kullanılırız 
liste4=['ali','veli','isik','ali','veli']
liste4.extend(['a','b',10])
print(liste4)

# reverse => liste içindeki elemanları tersine çevirir
liste6=['kivi','elma','muz']
liste6.reverse()
print(liste6)

# sort => sıralama yapmak için kullanılır(küçükten büyüğe)
liste7=[10,40,5,90,]
liste7.sort()
print(liste7)

# clear => listeyi temizler
liste7.clear()
print(liste7)

