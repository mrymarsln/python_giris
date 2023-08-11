#tek sayıların toplamını bulan program yaz

'''toplam=0
for sayi in range(1,6):
    toplam=+sayi
    if(sayi%2==1):
        print('sayıların toplamı:',toplam)'''
def tek_sayilarin_toplami(n):
    toplam = 0
    for i in range(1, n+1, 2):
        toplam += i
    return toplam

n = int(input("Bir sayı girin: "))
sonuc = tek_sayilarin_toplami(n)
print(f"1 ile {n} arasındaki tek sayıların toplamı: {sonuc}")

