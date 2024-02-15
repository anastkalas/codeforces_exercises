n, m = map(int, input().split())
if m==n:
    print("0")
elif m%2!=0 and m%3!=0:
    print("-1")
elif m % n == 0:
    count=0
    check=False
    while m>n:
        if(m/n)%2==0:
            m=m/2
            count=count+1
            check=True
        elif (m/n)%3==0:
            m=m/3
            count=count+1
            check=True
        else:
            check=False
            print(-1)
            break
    if check:
        print(count)
else:
  print("-1")