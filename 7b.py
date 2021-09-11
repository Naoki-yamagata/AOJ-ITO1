
while True:
    #入力
    n,x = map(int,input().split())
    if n == x == 0:
        break
    #全捜索くさい
    count = 0
    for i in range(n+1):
        for j in range(i):
            if 1 <= x-i-j <= j-1:
                count += 1

    print(count)