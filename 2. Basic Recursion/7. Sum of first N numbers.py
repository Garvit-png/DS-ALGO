# Parameterized way 

def f(i,sum):
    if i<1:
        print(sum)
        return 
    f(i-1,sum+i)

f(20,0)
    

# Functional way

def f(n):
    if (n==0):
        return 0
    return n + f(n-1)

print(f(10))