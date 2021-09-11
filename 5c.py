
while True:
    h,w = map(int,input().split())
    if w==h==0:
        break

    for i in range(h):
        #奇数行なら#から始める
        if i % 2 == 0:
            count=0
            while True:
                print("#",end="")
                count += 1
                if count == w:
                    print("")
                    break
                print(".",end="")
                count += 1
                if count == w:
                    print("")
                    break
        #偶数行なら.から始める
        if i % 2 != 0:
            count=0
            while True:
                print(".",end="")
                count += 1
                if count == w:
                    print("")
                    break
                print("#",end="")
                count += 1
                if count == w:
                    print("")
                    break
    print("")
        


