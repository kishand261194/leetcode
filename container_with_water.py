def maxArea(self, height):
    i=0
    j=len(height)-1
    _max=0
    while(i<j):
        curr=0
        if height[i]<height[j]:
            curr=height[i]*(j-i)
            i+=1
        else:
            curr=height[j]*(j-i)
            j-=1
        if _max<curr:
            _max=curr
    return _max
