
while True:
    m,f,r = map(int,input().split())
    #終了
    if m == f == r == -1:
        break

    #成績分け
    if m == -1 or f == -1:
        print("F")
    elif m+f >= 80:
        print("A")
    elif m+f >= 65:
        print("B")
    elif m+f >= 50:
        print("C")
    elif m+f >= 30 and r >= 50:
        print("C")
    elif m+f >= 30:
        print("D")
    else:
        print("F")
