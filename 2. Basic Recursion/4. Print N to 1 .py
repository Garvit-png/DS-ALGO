def f(i):
    if i<0:
        return 
    print(i,end=" ")
    f(i-1)

f(20)