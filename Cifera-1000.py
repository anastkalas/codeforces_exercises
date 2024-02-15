k=int(input())
l=int(input())
root=1
while k**(root)<l:
    root=root+1
 
if k**(root)==l:
    print("YES")
    print(root-1)
elif l==k:
    print("YES")
    print(0)
else:
    print("NO")