
a,b=map(int, input().split())
 
numbers=[]
numbers.append(b)
moves=0
 
while a<b:
    if b%10==1:
        b=(b-1)/10
    else:
    	b=b/2
    moves=moves+1
    numbers.append(int(b))
if a==b:
    print("YES")
    print(moves+1)
    numbers=numbers[::-1]
    print(*numbers)
else:
    print("NO")