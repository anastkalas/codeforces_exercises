t=int(input())
results=[]
for i in range(0,t):
    x,y,k=map(int, input().split())
    #1)how many sticks do i need for coals
    needed_sticks=k*y
    count=0#number of trades
    coal=0
    sticks=1
    while sticks<needed_sticks:
        sticks=(sticks-1)+x
        count=count+1
    count=count+k
    sticks=sticks-needed_sticks
    coal=coal+k
    while sticks<k:
        sticks=(sticks-1)+x
        count=count+1
    results.append(count)
    
for i in range(0,len(results)):
    print(results[i])
