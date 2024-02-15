n = int(input())
# Sort and reverse a list of coins in Python
list_of_coins = list(map(int, input().split()))
list_of_coins.sort() # Sort the list in place
list_of_coins.reverse() # Reverse the list in place
#print(list_of_coins)
 
#um of the coins
sumc=0
for i in range(0,len(list_of_coins)):
    sumc=sumc+list_of_coins[i]
 
 
sum=0
number_of_coins=0
for i in range(0,len(list_of_coins)):
    if i==0:
        sum=sum+list_of_coins[i]
        sumc=sumc-list_of_coins[i]
        number_of_coins=number_of_coins+1
    else:
        if sumc>=sum:
            sum=sum+list_of_coins[i]
            sumc=sumc-list_of_coins[i]
            number_of_coins=number_of_coins+1
        else:
            break
        
print(number_of_coins)