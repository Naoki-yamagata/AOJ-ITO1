buildings = [[[0 for x in range(10)]for y in range(3)]for z in range(4)]
n = int(input())
for i in range(n):
    b,f,r,v =map(int,input().split())
    buildings[b-1][f-1][r-1] += v

for i in range(4):
    for j in range(3):
        print(" ",end="")
        print(*buildings[i][j])
    if i == 3:
        break
    print("#"*20)
        
