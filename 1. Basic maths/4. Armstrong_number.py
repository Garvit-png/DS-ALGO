# Armstrong number mtlb , jo bhi number hai , uska jitna count hai, us sabhi numbers ke individual integers pe uski power lgake sum krke vohi number aana chahiye

# eg - 371
# 3^3 + 7^3 + 1^3 = 371

x=int(input())
length = len(str(x))
temp=x
is_armstrong = 0

while temp>0:
    d=temp%10
    is_armstrong+=d**length
    temp//=10

print(is_armstrong==x)


