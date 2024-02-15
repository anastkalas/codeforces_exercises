word=str(input())
hello = "hello"
i = 0
 
for letter in word:
    if i < len(hello) and letter == hello[i]:
        i += 1
 
if i == len(hello):
    print("YES")
else:
    print("NO")