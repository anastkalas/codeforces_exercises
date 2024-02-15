colors=list(map(int, input().split()))
check=0
check2=False
check4=False
check5=False
check6=False
check7=False
check8=False
 
if colors[0]==colors[1]:
    check=check+1
    check4=True
    
if colors[0]==colors[2]:
    check=check+1
    check7=True
    if check==2:
        check2=True
    
if colors[0]==colors[3]:
    check=check+1
    check5=True
    if check4==True and check5==True:
        check6=True
        
check1=0
 
if check<3:
    if colors[1]==colors[2] and check2==False:
        check=check+1
        check1=check1+1
        
    if colors[1]==colors[3] and check6==False:
        check=check+1
        check1=check1+1
        
if check<3 and check1<2 and check7==False and check5==False:
    if colors[2]==colors[3]:
        check=check+1
        
print(check)