arr=list(map(int,input().split()))

def f(l,r):
    if l>=r:
        return  
    arr[l],arr[r]=arr[r],arr[l]
    return f(l+1,r-1)

f(0,len(arr)-1)

print(*arr) # * star mtlb list ko unpack krna 

