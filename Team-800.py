n=int(input())
problems_solved=0
solved=0
 
for i in range(0,n):
    friends_to_solve = list(map(int, input().split()))
    for j in range(0,len(friends_to_solve)):
        if friends_to_solve[j]==1:
            problems_solved=problems_solved+1
    if problems_solved>=2:
        solved=solved+1
    problems_solved=0
print(solved)