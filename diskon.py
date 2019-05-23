'''
diskon harga
input :
    int : total_belanja
    
output:
    int : harga_bayar
    
proses:
read(x)
if x > 150000 then
    x = 0.9 * x
endif    
write(x)
'''

#cara 1
x = int(input("Total belanja = "))
#if x > 150000:
#    x *= 0.9    
#print("Harga bayar = {}".format(x))

#cara 2
x -= int(x > 150000) * 0.1 * x
print("Harga bayar = {}".format(x))