#string metodlar - upper() & lower()
gel_yaz='geleceği_yazanlar'
a=gel_yaz.upper()
print(a)
b=gel_yaz.lower()
print(b)

#soru sorar =>hepsi büyük mü? & hepsi küçük mü? - false ya da true cevap verir =>bool<=
c=gel_yaz.isupper()
print(c)
d=gel_yaz.islower()
print(d)

#len()->uzunluk =>str ifadenin elemen saysını gösterir 
print(len(gel_yaz))

#.replace()elimizdeki str ifadenin içindeki karakter değişikliği yapmak için kullanılır 
print(gel_yaz.replace('e','a'))#e harfini a ile değiştir

#.strip()=> başında ve sonunda parantez içine koyduğumuz nesne varsa onu siler 
gel_yaz='wgeleceği yazanlarw'
print(gel_yaz.strip('w'))

#.capitalize()=>ilk kelimenin ilk harfini büyük yap & .title()=>bütün kelimelerin ilk harfini büyük yap
print(gel_yaz.capitalize())
print(gel_yaz.title())

#substringler => elimizdeki strlerin alt kümelerini ele almak
print(gel_yaz[1]) # => 1. indexi yazar
print(gel_yaz[3:7]) # => 3. indexden 7. indexe kadar yazar (3. index dahil 7.index dahil değildir)

#DEĞİŞKENLER
a=9
b=9.2
c=1+2j

#tipleri(türleri)
print(type(a)) #int
print(type(b)) #float
print(type(c)) #complex

#TYPE_DÖNÜŞÜMLERİ
toplama_bir=10
toplama_iki=20

print(type(toplama_bir))
