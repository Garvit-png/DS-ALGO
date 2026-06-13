x=int(input())
reverse=0
while x>0:
    last_digit=x%10
    reverse=(reverse*10)+last_digit
    x//=10

print(reverse)





