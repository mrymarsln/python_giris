#sınıf nedir? -benzer özellikleri oratak amaçlar taşımak için gruplandırmak
class veri_bilimci():
    print('bu bir sınıftır')

#sınıf özellikleri(class attributes)
class veribilimci():
    bolum=''
    sql='evet'
    deneyim_yili=0
    bildiği_diller=[]
#sınıfların özelliklerine erişmek
print(veribilimci.bolum)
print(veribilimci.sql)
#sınıfların özelliklerini değiştirmek
veribilimci.sql='hayır'
print(veribilimci.sql)
#sınıf örneklendirmesi(instantiation)
ali=veribilimci() #ali tanımladığımız sınıfın bütün özelliklerini taşır
print(ali.sql)
print(ali.deneyim_yili)
print(ali.bolum)

ali.bildiği_diller.append('python') #!!!alinin bildiği dillere python eklendi ve bu değişiklik bütün sınıfı etkiledi!!!sınıfın genel değerlerini de değiştiriyor
print(ali.bildiği_diller)

veli=veribilimci()
print(veli.bildiği_diller) #bir adım yukarıda yaptığımız ekleme işlemi bütün sınıfı etkilediği için veli içinde tanımladığımız sınıf değişikliğe maruz kalmıştır 

#örnek özellikleri => örneklerin her birisini kendi içinde değşebilir olduğu bilgisini pythona verme 
#self => temsil edici
class veribilimci():
    bolum=''
    sql='evet'
    deneyim_yili=0
    bildiği_diller=['R','PYTHON']
    def __init__(self):
        self.bildiği_diller=[]
        self.bolum=''
ali=veribilimci() #KİŞİLEŞTİRİLMİŞ OLDUĞU İÇİN DEF OLAN BÖLÜMÜ ALIR
print(ali.bildiği_diller)

veli=veribilimci()
print(veli.bildiği_diller)

ali.bildiği_diller.append('PYTHON')
print(ali.bildiği_diller)

veli=veribilimci()
print(veli.bildiği_diller)

print(veribilimci.bildiği_diller) #DİREKT KİŞİLEŞTİRİLMEMİŞ VERİBİLİMİ BÖLÜMÜNÜ ALIR

#ÖRNEK METODLARI => örnek ve üzerinde çalışan fonksiyonları çalıştırır
class veribilimci(): #sınıf tanımlandı
    calisanlar=[] #veri bilimci sınıfının özelliklerini tanımlayacağımız özellik tanımladık 
    def __init__(self): #örnekler içinde birbirinden farklı değerler alabilecek şekilde nesne tanımladık
        self.bildiği_diller=[]
        self.bolum=''
    def dil_ekle(self, yeni_dil): #yeni özelliği otomatik olarak ekleme işlemi yaptırır
        self.bildiği_diller.append(yeni_dil)

ali=veribilimci()
veli=veribilimci()
print(ali.bildiği_diller)
print(ali.bolum)

print(veli.bildiği_diller)
print(veli.bolum)

print(dir(veribilimci))

ali.dil_ekle('R')
print(ali.bildiği_diller)

veli.dil_ekle('PYTHON')
print(veli.bildiği_diller)

#miras yapıları(inheritance)
class employees():
    def __init__(self):
        self.firstname=''
        self.lastname=''
        self.address=''

class datascience(employees):
    def __init__(self):
        self.programing=''

veribilimci1=datascience()
print(veribilimci1)

class marketing(employees):
    def __init__(self):
        self.storytelling=''

mar1=marketing()
print(mar1)

