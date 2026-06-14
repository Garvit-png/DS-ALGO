s="abba"

def f(i,s):
    n=len(s)
    if i>=n/2:
        return True
    if s[i]!=s[n-i-1]:
        return False
    return f(i+1,s)

print(f(0,s))

