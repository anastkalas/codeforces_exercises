w=int(input())
check=False
for i in range(1,w):
    
    if (w-i)%2==0 and i%2==0:
        check=True
        break
 
if check:
    print("YES")
else:
        print("NO")