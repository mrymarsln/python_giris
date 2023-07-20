# dictionary(sözlük) => kapsayıcı, sırasız, değiştirilebilir
sozluk={'REG':'regresyon modeli',
'LOJ':'LOJİSTİK REGRESYON',
'CART':'classification and reg'}
print(sozluk)
print(type(sozluk))
print(len(sozluk))

sozluk2={'REG':['rmse',10],
'LOJ':['mse',20],
'CART':['sse',30]}
print(sozluk2['REG'])

# sozluk => eleman eklemek & değiştirmek
sozluk={'REG':'regresyon modeli',
'LOJ':'LOJİSTİK REGRESYON',
'CART':'classification and reg'}

sozluk['GBM']='Gardien Boosting Mac' # eleman ekledi
print(sozluk)

sozluk['REG']='coklu sinir agları' # reg e sinir aglarını atadı
print(sozluk)

sozluk[1]='yapay sinir agları' # sozluk de 1 anahtarı olmadığı için yeni key ve value değeri ekledi
print(sozluk)

t=('tuple',)
sozluk[t]='yeni bir sey'
print(sozluk)

