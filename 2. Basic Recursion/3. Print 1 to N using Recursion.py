def f(i,n):
    if i>n:
        return 
    print(i,end=" ")
    f(i+1,n)

f(0,10)