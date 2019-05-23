a=1
b=5000
jml_gjl = jml_gnp = 0
for i in range(a,b):
    if i%2 == 1: jml_gjl += 1
    if i%2 == 0: jml_gnp += 1
    
print(jml_gjl, jml_gnp)