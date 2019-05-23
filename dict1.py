
mahasiswa = {
        2314: 'dede',
        9876: 'budi',
        '654x': 'heru'
    }
print(mahasiswa)
#print(mahasiswa[654])
#print(mahasiswa['654'])
print(654 in mahasiswa)
if 654 in mahasiswa:
    print(mahasiswa[654])
    
print('654' in mahasiswa)
if '654' in mahasiswa:
    print(mahasiswa['654'])
    
print('654' in mahasiswa and mahasiswa['654'] or '?')

mahasiswa[9876] = 'berta'
print(mahasiswa)

#mahasiswa.pop('654x')
#del mahasiswa['654x']
#print(mahasiswa)

mahasiswa['675434'] = 'dodi'