# Parametrised way========

def f(n,factorial):
    if n<=1:
        print(factorial)
        return 
    f(n-1,factorial*n)

f(5,1)


# Functional way=========

def f2(n):
    if n==0:
        return 1
    return n * f2(n-1)

print(f2(5))