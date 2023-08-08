#kullanıcıdan vize ve final notu al ve ortalamyı hesaplat.50 den düşük kaldı, 50-60 arası şartlı geçer, 60 üstü geçer
vize=float(input('vize notunuzu giriniz:'))
final=float(input('final notunuzu giriniz:'))
ortalama=float((vize*0.4)+(final*0.6))

if ortalama>=60:
    print('geçtiniz')
elif 60>ortalama>=50:  
     print('şartlı geçtiniz')
else:
    print('kaldınız')

