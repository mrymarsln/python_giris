#hatalar/istisnalar(exceptions)

#zerodivisionerror
a=10
b=0
try:
    print(a/b)
except ZeroDivisionError:
    print('payda da sifir olmaz')

#tip hatası
a=10
b='2'
try:
    print(a/b)
except TypeError:
    print('sayı ve string problemi')