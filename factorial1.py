import time

def fact(n):
#    if n == 0:
#        return 1
#    else:
#        return n * fact(n-1)
    return (n == 0) and 1 or (n * fact(n-1))

def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
#t0 = time.perf_counter()    
#print(fact(2))
#print(time.perf_counter()-t0)
#
#t0 = time.perf_counter()
#print(fact(5))
#print(time.perf_counter()-t0)
#
#t0 = time.perf_counter()
#print(fact(10))
#print(time.perf_counter()-t0)

x = fibo(35)