# word = input()
# temp = word

# def ispalindrome(l,r):                    # Wasted memory , not optmised , can be better
#     if l>=r:
#         return 
#         print(word==temp)
#     word[l],word[r]=word[r],word[l]
#     return ispalindrome(l+1,r-1)

# ispalindrome(0,len(word)-1)


word = input()
def ispalindrome(l,r):
    if l>=r:
        return True
    if word[l]!=word[r]:
        return False
    return ispalindrome(l+1,r-1)

print(ispalindrome(0,len(word)-1))
    
