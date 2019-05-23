#program menampilkan pola angka dgn loop

##basic for
for i in range(1,7):
    for j in range(1,7):
        if i % 2 == 0 or j % 2 == 0:
            print('0', end=' ')
        else:
            print('1', end=' ')
    print('')

#[ print(i, end=' ') for i in range(1,7) ]
#[ print(i, end=' ') for i in range(1,7) ]