#kullanıcıdan üç sayı al aldığın sayılardan en büyüğünü buldur
a=int(input('sayı giriniz:'))
b=int(input('sayı giriniz:'))
c=int(input('sayı giriniz:'))
if a>b and a>c:
    print('sayıların en büyüğü a')
elif b>c and b>a:
    print('sayıların en büyüğü b')
else:
    c>a and c>b
    print('sayıların en büyüğü c')

