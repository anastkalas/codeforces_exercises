username=str(input())
distinct_characters=[]
for i in range(0,len(username)):
    if i==0:
        distinct_characters.append(username[i])
    else:
        check=True
        for j in range(0,len(distinct_characters)):
            if username[i]==distinct_characters[j]:
                check=False
        if check==True:
            distinct_characters.append(username[i])
 
if len(distinct_characters)%2!=0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")