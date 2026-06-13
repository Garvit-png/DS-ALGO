x=int(input())
temp=x
reverse=0


while temp>0:
    last_digit=temp%10
    reverse=(reverse*10)+last_digit
    temp//=10


if reverse==x:
    print("Yes")
else:
    print("No")



