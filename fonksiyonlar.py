# def=fonksiyon tanımlama 
def kare_al(x):
    print(x**2)
kare_al(3)

def kare_al(x):
    print('girilen sayının karesi:' +str(x**2))
kare_al(4)    

def kare_al(x):
    print('girilen sayi:' + str(x) +', karesi:'+str(x**2))
kare_al(5)    

#iki argümanlı fonksiyon tanımlamak
def carpma_yap(x,y):
    print(x*y)
carpma_yap(2,3)

#ön tanımlı argümanlar
def carpma_yap(x, y=1):
    print(x*y)
carpma_yap(3)

def carpma_yap(x, y=1):
    print(x*y)
carpma_yap(3,4)

# neden fonksiyon? -sık tekrar eden uzun işlemlerden kurtulmak için 
def direk_hesap(isi, nem, sarj):
    print((isi+nem)/sarj)
direk_hesap(30,40,50)


# RETURN => çıktıyı girdi olarak kullanmak 
def direk_hesap(isi, nem, sarj):
    return((isi+nem)/sarj)
cikti=direk_hesap(25,40,90)
print(cikti)
direk_hesap(25,40,90)*9

# LOCAL VE GLOBAL değişkenler
#local => bir fonksiyonun ya da döngünün etkisinde olan değişkenler
#global => ana çalışma alanımız dışındakiler  
x=10
y=20
def carpma_yap(x=2,y=3):
    return x*y
print(carpma_yap(2,3))

#local etki alanından global etki alanını değiştirmek
x=[]
def eleman_ekle(y):
    x.append(y)
    print(str(y) + ' ifadesi eklendi')
eleman_ekle('ali')
eleman_ekle('veli')

# if => eğer
sinir=5000
gelir=6000
if gelir > sinir: # eğer bu şart sağlanıyorsa yazdırma işlemi yapar
    print('gelir sinirdan büyüktür')

# else => değil ise
sinir=5000
gelir=4000
if gelir > sinir: 
    print('gelir sinirdan büyüktür')
else:
    print('gelir sinirdan küçüktür')

# elif => birden fazla koşul kullandığımızda kullanırız
sinir=5000
gelir1=6000
gelir2=5000
gelir3=3500
if gelir1>sinir:
    print('tebrikler, hediye kazandınız')
elif gelir1<sinir:
    print('uyarı!')
else:
    print('takibe devam')


if gelir3>sinir:
    print('tebrikler, hediye kazandınız')
elif gelir3<sinir:
    print('uyarı!')
else:
    print('takibe devam')


if gelir2>sinir:
    print('tebrikler, hediye kazandınız')
elif gelir2<sinir:
    print('uyarı!')
else:
    print('takibe devam')

#MİNİ UYGULAMA
Sinir=50000
magaza_adi=input('magaza adi nedir?')
gelir=int(input('gelirinizi giriniz:'))

if gelir<sinir:
    print('tebrikler:' + magaza_adi +' promosyon kazandınız!')
elif gelir<sinir:
    print('uyarı! cok dusuk gelir:' + str(gelir))
else:
    print('takibe devam')