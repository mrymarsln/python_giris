# set(küme) => sırasız(indexlenemez), değerleri eşsizdir, değiştirilebilir, farklı tipler barındırabilir
s=set()
print(type(s))
# liste üzerinden set oluşturma
l=[1,'a','ali']
print(type(l))
s=(set(l))
print(s)
# tuple üzerinden set oluşturma 
t=('a','ali')
s=set(t)
print(s)

#her bir karakteri bir kere yazdırır
ali='lütfen_ata_bak ma_uza ya_git'
print(type(ali))
s=set(ali)
print(s)

l=['ali','lutfen','ata','bakma','uazaya','git','git','ali','git']
print(type(l))
s=set(l)
print(s)
print(len(s)) #aynı olan karakterli sadece 1 kere sayar

# eleman ekleme & silme
l=['geleceği','yazanlar']
s=set(l)
print(s)
print(dir(s)) # metodlara erişir

s.add('ile') # ile elemanını ekler
print(s)
s.add('gelecege_git')
print(s)

s.remove('ile')# ile elemanını siler
print(s)

#difference & symmetric_difference
set1=set([1,3,5])
set2=set([1,3,2])
print(set1.difference(set2)) #set1 de olup set2 de olmayanı yazdırır
print(set2.difference(set1)) #set2 de olup set1 de olmayanı yazdırır

print(set1.symmetric_difference(set2)) #ikisinde de farklı olanı çalıştırır
print(set2.symmetric_difference(set1)) # ikisinde de farklı olanı çalıştırır

print(set1-set2)
print(set2-set1)
 
# intersection & union
set1=set([1,3,5])
set2=set([1,2,3])

print(set1.intersection(set2)) # set1 ve st2 nin kesişimlerini alır
print(set2.intersection(set1)) # set1 ve st2 nin kesişimlerini alır

kesisim=set1 & set2  # set1 ve st2 nin kesişimlerini alır
print(kesisim)

birlesim=set1.union(set2) #set1 ve st2 nin birleşimlerini alır
print(birlesim)

set1.intersection_update(set2) 
print(set1)

# set sorgu işlemleri
set1=set([7,8,9])
set2=set([5,6,7,8,9,10])
#iki kümenin kesişiminin boş olup olmadığının sorgulanması
print(set1.isdisjoint(set2))

# bir kümenin bütün elemanlarının başka bir küme içerisinde yer alıp almadığı
print(set1.issubset(set2)) # set1 set2 nin alt kümesi mi?

# bir kümeyi kapsayıp kapsamadığı
print(set2.issuperset(set1)) # set2 set1 i kapsıyor mu?

