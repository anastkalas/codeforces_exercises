n=int(input())
goals=[]
 
for i in range(0,n):
  goal=str(input())
  goals.append(goal)
 
goals.sort()
teama=goals[0]
teamac=1
teambc=0
 
for g in range(1,len(goals)):
    if goals[g]==teama:
        teamac=teamac+1
        
    else:
        teamb=goals[g]
        teambc=teambc+1
    
 
if teamac>teambc:
    print(teama)
else:
    print(teamb)