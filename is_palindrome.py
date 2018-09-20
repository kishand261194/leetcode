def isPalindrome(x):
    num=str(x)
    flag=True
    h=0
    str_len=len(num)
    for i, j in zip(num, num[::-1]):
        if h>str_len/2:
            break
        if i!=j:
            flag=False
            break
        h+=1
    return flag
print(isPalindrome(-121))
