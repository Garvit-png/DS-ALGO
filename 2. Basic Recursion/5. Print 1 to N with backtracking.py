def f(i):
    if i<0:
        return
    f(i-1)
    print(i)

f(20)