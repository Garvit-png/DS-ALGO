# GCD HCF --

# assume 

# 9 - 1, 3, 9
# 12 - 1, 2, 3, 4, 6, 12
# highest common factor is 3

# 11 - 1, 11
# 13 - 1, 13 
# highest common factor is 1


# a,b=map(int,input().split())
# hell = 0
# for i in range(1,min(a,b)+1):
#     if a%i==0 and b%i==0:
#         hell=i

# print(hell)



a,b=map(int,input().split())
for i in range(min(a,b),0,-1):
    if a%i==0 and b%i==0:
        print(i)
        break



