# Prime number - No. which is divisible by 1 and itself - this is wrong ❌

# Prime number - No. which have only 2 factors - this is write ✅


# 11 - 1, 11 (yes)
# 7 - 1, 7(yes)
# 12 - 1, 2, 3, 4, 6, 12(no)


# x=int(input())
# count=0
# for i in range(1,x+1):
#     if x%i==0:
#         count+=1
# if count==2:
#     print(f"yes {x} is a prime")
# else:
#     print(f"no {x}  not a prime")



import math
x=int(input())
count=0
for i in range(1,int(math.sqrt(x)+1)):
    if (x%i==0):
        count+=1
        if ((x/i)!=i):
            if x%(x/i)==0:
                count+=1
if count==2:
    print("Yes")
else:
    print("no")