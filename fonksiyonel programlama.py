#PYTHON'DAFONKSİYONEL PROGRAMLAMA => esnek,bizi daha iyi anlayabilen programlama yaklaşımıdır
#1-fonksiyonlar dilin baştacıdır(birinci sınıf nesnelerdir)
#2-yan etkisiz fonksiyonlar. (stateless, girdi-çıktı)
#3-yüksek seviyeli fonksiyonlar
#4-vektörel operasyonlar

#yan etkisiz fonksiyonlar(pure functions)
#örnek1:Bağımsızlık

A=9 #global etki alanı
def impure_sum(b):
    return b+A
def pure_sum(a,b):
    return a+b

print(impure_sum(6))
print(pure_sum(3,4))
#örnek2: ölümcül yan etkiler
#oop
#fp

#isimsiz fonksiyonlar(anonymous functions) =>isimlendirme yapmadan fonksiyon tanımlamak
new_sum=lambda a,b:a+b
new_sum(4,5)
sırasız_liste=[('b',3),('a',8),('d',12),('c',1)]
print(sorted(sırasız_liste, key=lambda x: x[1]))
print(sırasız_liste)

#vektörel operasyonlar(vectorel operations)
#oop
a=[1,2,3,4]
b=[2,3,4,5]

ab=[]

range(0,len(a))
for i in range (0,len(a)): #0'dan a'nın içinde ne kadar eleman varsa gezin
    ab.append(a[i]*b[i])
print(ab)

#fp(faktöriyel programlama)
'''import numpy as np
a=np.array([1,2,3,4])
b=np.array([2,3,4,5])
print(a*b)'''

#map & filter & reduce

#map 
liste=[1,2,3,4,5]
for i in liste:
    print(i+10)

print(list(map(lambda x:x*10, liste))) #=> verilen bir nesnenin üzerinde tanımlanacak bir fonksiyonu çalıştırır

#filter=> iteratif nesne alır
liste=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x :x%2==0,liste)))

#reduce(indirgeme)
from functools import reduce
liste =[1,2,3,4]
print(reduce(lambda a,b: a+b,liste))