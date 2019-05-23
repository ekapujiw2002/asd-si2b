
bil = int( input("Masukkan angka : "))
'''
if bil % 2 == 0:
    print("Bilangan genap")
    print("OK")
elif bil % 3 ==0:
    print("Bilangan kelipatan 3")
else:
    print("Bilangan ganjil")
'''

if not bil % 2:
    print("Bilangan genap")
    print("OK")
elif not bil % 3:
    print("Bilangan kelipatan 3")
else:
    print("Bilangan ganjil")    