n,m = map(int, input().split())
f = 0
for i in range(0,n):
    l = input().split()
    if 'C' in l or 'M' in l or 'Y' in l:
        f = 1
 
if f == 1:
    print("#Color")
else:
    print("#Black&White")