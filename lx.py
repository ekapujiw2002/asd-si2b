#[print("* "*(5-i), "+ "*(i)) for i in range(1,6)]
#
#[print("%s%s"%("* "*(5-i), "+ "*(i))) for i in range(1,6)]
#
#def gen_list():
#    lx=[]
#    for i in range(1,1001):
#        lx.append(chr( ord('a') + ((i-1)%26)))
#        lx.append(i)
#    return lx
#print(gen_list())

lx = []
[
    [
        lx.append(chr( ord('a') + ((i-1)%26))),
        lx.append(i)
    ]
    for i in range(1,1001)
]
print(lx)