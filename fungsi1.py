luas = 0

def luasSegitiga(tinggi=0,alas=0):
    try:
        #    global luas
    
    #    return
    #    pass
        
    #    return alas*tinggi/2
        print("tinggi = %f\talas = %f" % (tinggi, alas))
    #    print("tinggi = {}\talas = {}".format(tinggi, alas))
    #    print(tinggi,alas)
        luas = alas*tinggi/2
    #    print(luas)
        
        
    #    print(luas)
        
        return luas
    except Exception as err:
        pass
        return -1
    


def loopLuasSegitiga(tinggi=0,alas=0,jml_loop=1):
#    for i in range(0,jml_loop):
#        print("%u = %f" % (i,luasSegitiga(tinggi, alas)))
    [print("%u = %f" % (i,luasSegitiga(tinggi, alas)))
 for i in range(0, jml_loop)]

print(luasSegitiga())
print(luasSegitiga(0.5))
print(luasSegitiga("jdajfhait",0.5))
print(luasSegitiga(alas=0.5))
#
#print(luas)
print(luasSegitiga(0.5,2))
print(luasSegitiga(alas=0.5,tinggi=5))
#print(luas)
#
#print(luasSegitiga(alas=0.5, tinggi=5))
#loopLuasSegitiga(2, 3, 3)

#while True:
#    print(luasSegitiga(
#        float(input("Tinggi = ")),
#        float(input("Alas = "))
#        ))
#    if input("Ulangi [Y/T]? ").lower() != 'y':
#        break

#for i in range(1,6):
#    for j in range(1,4):
#        print(luasSegitiga(i,j))

print("LIST LOOP CALL")
[print(luasSegitiga(i,0.5)) for i in range(0,5)]        