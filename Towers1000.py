#bars can be put on top of the other if their lengths are the same
#goal=print height of the largest tower and their total number of towers
n=int(input())#number of bars
lengths=list(map(int, input().split()))
lengths.sort()
heights=[]
h=1
for i in range(0,len(lengths)):
    if i<len(lengths)-1:
        if lengths[i]==lengths[i+1]:
            h=h+1
        else:
            heights.append(h)
            h=1
    else:
        heights.append(h)
for i in range(0,len(heights)):
    if i==0:
        mx=heights[i]
    else:
        if mx<heights[i]:
            mx=heights[i]
print(mx, len(heights))
