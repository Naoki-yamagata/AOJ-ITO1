N =int(input())
ans = []
for i in range(1,N+1):
    if "3" in str(i) or i%3==0 :
        ans.append(i)
print(" ",end="")
print(*ans)