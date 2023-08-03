#for döngüsü => iteratif(tekraralan) bir şeyler yapmak istediğimizde 
ogrenci=['ali','veli','isik','berk']
for i in ogrenci: #i eleman temsil etmek
    print(i)

maaslar=[1000,2000,3000,4000,5000]
for a in maaslar: #a eleman temsil etmek
    print(a)

#maaslara yüzde yirmi zam yapılacak gerekli kodları yaz
#1- fonksiyonu tanımla
#2-döngüyü yaz
def yeni_maas(x):
    print(x*20/100+x)
for i in maaslar:
    yeni_maas(i)

#maası 3000 tl den fazla olanlara yüzde on zam, 3000 tl den az olanlara yüzde yirmi zam yap
maaslar=[1000,2000,3000,4000,5000]
def maas_ust(x):
    print(x*10/100+x)
def maas_alt(x):
    print(x*20/100+x)
for i in maaslar:
    if i >=3000:
        maas_ust(i)
else:
    maas_alt(i)

#berak & continue ifadeleri
maaslar=[8000,5000,2000,1000,3000,7000,1000]
dir (maaslar)
maaslar.sort()
print(maaslar)
#break => girdiğimiz değere kadar olan döngüyü devam ettir sonra kes
for i in maaslar:
    if i ==3000:
        print('kesildi')
        break
    print(i)
#continue => girdiğimiz değere işlem yapmadan atla
for i in maaslar:
    if i ==3000:
        continue
    print(i)

#while döngüsü => bu şart sağlandığı sürece döngüyü devam ettir. -olduğu sürece
sayi=1
while sayi < 10: #sayi 10 dan küçük olduğu sürece 
    sayi+=1      #1 ekle yazdır
    print(sayi)