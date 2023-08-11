#!!! 1 den 100 e kadar olan sayıların toplamını bulan programı yaz
toplam = 0

for sayi in range(1, 101): #range belirli bir aralıkta bulunan sayıları göstermek için ->1,2,3,...,100 (101 dahil değil)
    toplam += sayi

print(f"1'den 100'e kadar olan sayıların toplamı: {toplam}")
