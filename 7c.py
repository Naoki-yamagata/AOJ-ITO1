
r,c =map(int,input().split())

#行列入力
gyo = [0 for i in range(r)]
for i in range(r):
    gyo[i] = list(map(int,input().split()))

#各行の最後に行の合計を追加
for i in range(r):
    gyo[i].append(sum(gyo[i]))

#各列の合計を表す行を書く
Sum = []
for i in range(c+1):
    S = 0
    for j in range(r):
        S += gyo[j][i]
    Sum.append(S)

for i in range(r):
    print(*gyo[i])
print(*Sum)