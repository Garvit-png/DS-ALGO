# gcd(n1, n2) = gcd(n1-n2, n2)

# pattern is we keep dividing it , and at the end , we are getting remainder only


a,b=map(int,input().split())

while (a>0 and b>0):
    if (a>b):
        a=a%b
    else:
        b=b%a

    if a==0:
        print(b)
    else:
        print(a)