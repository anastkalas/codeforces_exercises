string=str(input())
string=string.lower() 
 
listofvowels=['a','e','i','o','u','y']
 
emptystring=''
count=0
for i in range(0,len(string)):
    check=False
    for j in range(0,len(listofvowels)):
        if string[i]==listofvowels[j]:
            check=True
            break
    if check==False:
        count=count+1
        if count==1:
            emptystring=emptystring+"."+string[i]
        else:
            emptystring=emptystring+"."+string[i]
        
print(emptystring)