'''
konversi detik
input	: detik
output	: jam, menit, detik
execute dengan :
c:\Python34\python.exe konv-detik.py
'''

# 1. baca total detik dari user
try:
    detik = int(
        input("Masukkan durasi dalam detik : ")
    )
except:
    pass
    detik = 0
    print("ANDA GILAAAAAA!!!!")
    
    
#print(type(detik))
#print(detik)

# 2. ubah detik ke jam, menit, detik
#jam = detik/3600
#print(jam)

jam = detik//3600
menit = (detik % 3600)//60
detik = detik % 60
#detik %= 60

# 3. print hasil
#print(jam,menit,detik)
print("%02u:%02u:%02u"%(jam, menit, detik))