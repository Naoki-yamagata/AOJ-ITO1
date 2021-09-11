n,m=map(int,input().split())

#行列入力
gyo = [0 for i in range(n)]
for i in range(n):
    gyo[i] = list(map(int,input().split()))

#ベクトル入力
vector = []
for i in range(m):
    vector.append(int(input()))

#計算
ans = []
for i in range(n):
    sum = 0
    for j in range(m):
        sum += gyo[i][j]*vector[j] 
    ans.append(sum)

#解答出力
for i in ans:
    print(i)