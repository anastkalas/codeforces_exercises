n=int(input())
array=list(map(int, input().split()))
if n!=1:
    array.sort()
    first_half_length=len(array)//2
    first_half=[]
    second_half=[]
    for i in range(0,len(array)):
        if i<first_half_length:
            first_half.append(array[i])
        else:
            second_half.append(array[i])
    second_half=second_half[::-1]
    sh=0
    fh=1
    new_list=[]
    for i in range(0,len(array)):
        if i==0:
            new_list.append(first_half[0])
        elif i%2==0 and fh<len(first_half):
            new_list.append(first_half[fh])
            if fh+1<len(first_half):
                fh=fh+1
        else:
            new_list.append(second_half[sh])
            if sh+1<len(second_half):
                sh=sh+1
    print(*new_list, sep=' ')
elif n==1:
    print(*array,sep=' ')