def longestPalindrome(s):
    str_len=len(s)
    arr=[[None for i in range(str_len)] for i in range(str_len)]
    longest_i=None
    longest_j=None
    max_lenght=-1
    for lenght in range(str_len):
        i = 0
        j = lenght
        while(j<str_len):
            if (i==j):
                arr[i][j]=True
                if (j-i)+1 > max_lenght:
                    longest_i = i
                    longest_j = j
                    max_lenght=(j-i)+1
            elif (s[i]==s[j] and arr[i+1][j-1]==True or ((s[i]==s[j]) and lenght==1 ) ):
                arr[i][j]=True
                if (j-i)+1 > max_lenght:
                    longest_i = i
                    longest_j = j
            else:
                arr[i][j]=False
            j+=1
            i+=1
    return s[longest_i:longest_j+1]
print(longestPalindrome('abbbba'))
