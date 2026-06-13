# x=int(input())
# for i in range(1,x+1):
#     if x%i==0:
#         print(i,end=" ")

# TC - O(N)
#SC - O(1)



# to save the time we will use sqrt method because after origin, the things starts to repeat 

#eg - 36

# 1 * 36
# 2 * 18
# 3 * 12
# 4 * 9
# 6 * 6
# ------
# 9 * 4 
# 12 * 3
# 18 * 2
# 36 * 1


# unsorted 
# import math
# x=int(input())
# for i in range(1,int(math.sqrt(x))+1):
#     if x%i==0:
#         print(i,end=" ")
#         if (int(x/i)!=i):     #yeh isiliye lgai because agr upr 6 * 6 ke case mein 6 print hogya, and niche bhi 6 aagye toh use ignore krdo
#             print(int(x/i),end=" ")

# sorted
import math
x=int(input())
list=[]
for i in range(1,int(math.sqrt(x)+1)):
    if (x%i)==0:
        list.append(i)
        if (int(x/i)!=i):
            list.append(int(x/i))


print(sorted(list))


    