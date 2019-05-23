print("PROGRAM RANGE ANGKA")
x = int(input("Angka = "))
#if x >= -5 and x <= -1:
#    print("LEVEL 1")
#elif x >= 0 and x <= 5:
#    print("LEVEL 2")
#elif x > 5:
#    print("LEVEL 3")
#else:
#    print("???")

if -5 <= x <= -1:
    print("LEVEL 1")
elif 0 <= x <= 5:
    print("LEVEL 2")
elif x > 5:
    print("LEVEL 3")
else:
    print("???")