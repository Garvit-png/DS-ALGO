# Parameterized way

def f(i,factorial):
    if i<1:
        print(factorial)
        return 
    f(i-1,factorial*i)

f(5,1)


# Functional way

def f(n):
    if n==0:
        return 1
    return n * f(n-1)
print(f(5))