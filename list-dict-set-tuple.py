'''
list, tuple, set, dict
'''

def kali(a,b):
    return a*b

#LIST
list1 = [34, 12, 'hello world', -324, 0.24245, 'ini kalimat', kali,
         range(0,25)]
print(list1)
print(list1[1])
list1[3] = [1,6,5]
print(list1)

list1.append('ini item baru')
print(list1)

list1.insert(1, 'ini item di index 1')

#pop = ambil lalu remove
list1.pop(1)

#cari value (harus sama)
list1.index(12)

pola = [
    print("%s%s" % ("* "*i, "- "*(5-i)))
    for i in range(0,6)
    ]
pola1 = [
    ["%s%s" % ("* "*i, "- "*(5-i))]
    for i in range(0,6)
    ]