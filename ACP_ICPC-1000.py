scores=list(map(int, input().split()))
scores=sorted(scores)
suma=sum(scores)

def permutations(word):
    if len(word)==1:
        return [word]
    #Recursively call permutations function on the word without its first character
    perms=permutations(word[1:])
    #get the first character of the word
    char = word[0]
    #Initialize an empty list to store the permutation
    result=[]
    #Iterate over each permutation generated from the racursive call
    for perm in perms:
        #Iterate over each position in the current permutation plus one(to include the character at the begining)
        for i in range(len(perms)+1):
            #Insert the character at the current position and append the modified permutation to the result list
            result.append(perm[:i]+[char]+perm[i:])
    #Return the list of permutation
    return result

if suma%2==0:
    scores=permutations(scores)
    count=0
    teama=0
    teamb=0
    pointh=1
    point=5
    i=0
    while count<5:
        if i==0:
            teama=teama+scores[i]
            teamb=teamb=+scores[point]
            i=i+1
            pointh=pointh+1
            point=point-pointh
        else:
            if teama>teamb:
                teamb=teamb+scores[point]
                pointh=pointh+1
                point=point-pointh
            elif teama<teamb:
                teama=teama+scores[i]
                i=i+1
            else:
                teama=teama+scores[i]
                i=i+1
        count=count+1
    if teama==teamb:
        print("YES")
    else:
        print("NO")
else:
    print("NO")


