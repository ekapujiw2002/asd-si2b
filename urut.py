'''
input:
    int: a,b,c
    
output:
    urutan angka dari terkecil sd terbesar
    
algoritma:
read(a)
read(b)
read(c)

if a<b and a<c:
    write(a)
    if b<c:
        write(b)
        write(c)
    elif b>c:
        write(c)
        write(b)
    else:
        write(b)
        write(c)
elif b<a and b<c:
    write(b)
    if a<c:
        write(a)
        write(c)
    elif a>c:
        write(c)
        write(a)
    else:
        write(a)
        write(c)
elif c<a and c<b:
    write(c)
    if a<b:
        write(a)
        write(b)
    elif a>b:
        write(b)
        write(a)
    else:
        write(a)
        write(b)
else
    write(a)
    write(b)
    write(c)
'''