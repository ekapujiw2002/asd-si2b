'''
Fungsi untuk membandingkan 2 buah variabel
Parameter :
    a object variabel ke-1
    b object variabel ke-2
'''
def isEqual(a, b):
    return a==b

print(isEqual(3,5))
print(isEqual(3,3))
print(isEqual(3,'3'))
print(isEqual('3','3'))
print(isEqual('32abg','32aBg'))
print(isEqual([1,4,5],[1,3,5]))
print(isEqual(None, None))