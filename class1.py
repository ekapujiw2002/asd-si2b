class klas_induk:
    _id = 1
    _nama = 'induk'
    _element = []
#    pass

    def __init__(self):
        print("init")

    def plus(self):
        print("fungsi plus")
        
    def minus(self,a,b):
        print("fungsi minus")
        return a-b

def plus1():
    print("fungsi plus")

k1 = klas_induk()
#k2 = [klas_induk for i in range(1,6)]
k1.plus()

##[print('%s%s'%('*'*(5-i),'+'*i)) for i in range(1,6)]
#
#l = []
#for i in range(1,1001):
##    l.append([chr(ord('a')+(i%26)), i])
#    l.append(chr(ord('a')+(i%26)-1))
#    l.append(i)
#print(l)    