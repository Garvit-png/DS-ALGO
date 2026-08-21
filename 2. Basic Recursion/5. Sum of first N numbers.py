# There are 2 ways to solve this question - PARAMETRISED , FUNCTIONAL 

# Parametrised======================

def summy(i,summ):
    if (i<1):
        print(summ)
        return 
    summy(i-1,summ+i)

summy(20,0)



# Functional==================

def summation(n):
    if n==0:
        return 0 
    return n + summation(n-1)

print(summation(10))