n,m,l=map(int,input().split())

#行列1入力
gyo_1 = [0 for i in range(n)]
for i in range(n):
    gyo_1[i] = list(map(int,input().split()))

#行列2入力
gyo_2 = [0 for i in range(m)]
for i in range(m):
    gyo_2[i] = list(map(int,input().split()))
#ここまでOK

ans = [[0 for j in range(l)] for i in range(n)]

for i in range(n):
    for j in range(l):
        Sum = 0
        for k in range(m):
            Sum += gyo_1[i][k] * gyo_2[k][j]
        ans[i][j] = Sum
    
for i in range(n):
    print(*ans[i])