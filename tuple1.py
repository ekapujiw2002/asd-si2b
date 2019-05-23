t1 = ('hello',"world",'monday')
print(type(t1), len(t1), t1, t1[0])

def f1(a,b,c):
    return a, b, c, a*b**c

t3 = 4,5,6,23
r1 = f1(1,2,4)
print(r1)

t4 = 'a',5,'hello',f1, t3, ['hi','45',3.421,0xab]
