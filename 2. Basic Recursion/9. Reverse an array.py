arr=[1,2,3,4,5]


# Parameterized

# def f(l,r):
#     if l>=r:
#         return arr
#     arr[l],arr[r]=arr[r],arr[l]
#     return f(l+1,r-1)
# print(f(0,len(arr)-1))

# Functional 
def f(i):
    n=len(arr)
    if i>=n/2:
        return arr
    arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
    return f(i+1)
print(f(0)) 
