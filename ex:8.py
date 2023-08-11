#alınan stringi tersten yazdır
def ters_cevir(string):
    return string[::-1]
girilen_str=input('bir string girin:')
tersten_str=ters_cevir(girilen_str)
print('stringin ters çevrilmiş hali:',tersten_str)


