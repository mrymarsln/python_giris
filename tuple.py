# tuple(demet) => kapsayıcı (farklı türden verileri bir arada tutabilir), sıralı ve değiştirilemez
# aşşağıda ki iki ifadetuple değişkenini ifade eder
t=('ali','veli',1,2,3.2,[1,2,3,4])
t='ali','veli',1,2,3.2,[1,2,3,4]
print(type(t))

t2=('ali',) # tek değişkenli tuple ı ifade etmek istersek yanına virgül koymalıyız
print(type(t2))

t3=('ayse','fatma',1,2,3.4,[1,2,3])
print(t3[1])
print(t3[0:3])